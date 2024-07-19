from dataclasses import dataclass, field
import re
from typing import Callable, Dict, List, Tuple, TypedDict, ParamSpec
from rich.progress import Progress, TaskID
from itertools import accumulate, chain


from .progress_sync import ProgressSync
from .block_collections import BlockCollection as _BlockCollection, Blocks as _Blocks


def advance(progress:Progress, *tasks:TaskID, advance:int=1):
	for task in tasks:
		progress.update(task, advance=advance)



def passthrough_namer(flag:str) -> str:
	return flag

FlagDefinition = _BlockCollection|Dict[int, _BlockCollection]|Dict[float, _BlockCollection]
MapEntry = TypedDict('MapEntry', {'id':int, 'flags':frozenset[str], 'blocks':_BlockCollection})
FlagEntry = List[str|Tuple[str, List[int|float]]] 
@dataclass(frozen=True)
class BlockMapping:
	"""A mapping of block categories to block IDs"""
	mapping:List[MapEntry]
	flags: FlagEntry
	pragma:str = "BLOCK_ID_MAPPING"
	defines:Dict[str, str] = field(default_factory=dict)
	function_namer:Callable[[str], str] = passthrough_namer

	@classmethod
	def _expand(cls, flags:Dict[str, _BlockCollection|Dict[int, _BlockCollection]|Dict[float, _BlockCollection]]) -> Tuple[Dict[str, _BlockCollection], FlagEntry]:
		sequence_flags = {flag:values for flag, values in flags.items() if isinstance(values, dict)}
		bool_flags = {flag:values for flag, values in flags.items() if isinstance(values, _BlockCollection)}

		key_entries:FlagEntry = [(key, list(value.keys())) for key, value in sequence_flags.items()]
		key_entries.extend(bool_flags.keys())

		for to_expand, values in sequence_flags.items():
			seen = _Blocks({})
			for i, value in values.items():
				overlap = seen & value
				if overlap:
					raise ValueError(f"Sequence flag {to_expand} has ambiguous return values for the following blocks: {overlap}")
				bool_flags[f'{to_expand}.{i}'] = value
				seen += value
		return bool_flags, key_entries

	@classmethod
	def solve(
		cls, 
		flags:Dict[str, FlagDefinition], 
		* , 
		start_index:int=1000, 
		pragma:str="BLOCK_ID_MAPPING", 
		defines:Dict[str, str]|None = None,
		function_name:str|Callable[[str], str] = '{flag}'
	):
		"""Solve for a set of IDs that can be used to check if a block is in the specified categories
		
		Flag types:
		- Blocks: Produces the method `bool flag(int id)` that returns true if the block is in the given collection
		- Dict[int, Blocks]: Produces the method `int flag(int id)` that returns the key of the collection that the block is in, or 0 if the block is not in any of them.
		- Dict[float, Blocks]: Produces the method `float flag(int id)` that returns the key of the collection that the block is in, or 0.0 if the block is not in any of them.

		Args:
			flags: A dictionary of flag names to collections of blocks
			start_index: The first index to use for the block IDs
			pragma: The define used to prevent double-inclusion
			defines: A dictionary of defines to add to the generated code (useful for enum-like flags)
			function_name: Determines the name of the decoder function. If a string, it will be formatted with the flag name. If a callable, it will be called with the flag name.
		"""
		mapping:Dict[frozenset[str], _BlockCollection] = dict()
		encountered:_BlockCollection = _Blocks({})
		for flag_name in flags.keys():
			if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", flag_name):
				raise ValueError(f"Illegal identifier name '{flag_name}'")
		bflags, flag_entries = cls._expand(flags)
		expected_lengths = [*accumulate(range(len(bflags)), lambda x, _: 2 * x + 1, initial=0)]
		with Progress(transient=True) as progress:
			global_task = progress.add_task(total = sum(expected_lengths), description="Solving flag combinations")
			for index, (new_flag, new_values) in enumerate(bflags.items()):
				subtask = progress.add_task(total=expected_lengths[index], description=f"Adding {new_flag} ({index + 1} / {len(bflags)})")
				generators = ProgressSync(
					chain(
						[(frozenset([new_flag]), new_values.difference, encountered)],
						((frozenset([*combo, new_flag]),values.intersection, new_values) for combo, values in mapping.items()),
						((combo, values.difference, new_values) for combo, values in mapping.items()),
					),
					progress, 
					global_task,
					subtask
				)
				mapping = {key:val for key, operation, arg in generators if bool(val := operation(arg))}
				encountered = encountered.union(new_values) if encountered else new_values
				if index < len(bflags) - 1:
					expected_lengths[index + 1:] = [*accumulate(range(len(expected_lengths[index + 1:])), lambda x, _: 2 * x + 1, initial=len(mapping))]
					progress.update(global_task, total=sum(expected_lengths))
				progress.remove_task(subtask)
		return cls(
			[MapEntry(id=index + start_index, flags=key, blocks=val) for index, (key, val) in enumerate(mapping.items())], 
			flag_entries,
			pragma,
			defines or dict(),
			function_name if callable(function_name) else passthrough_namer if function_name == '{flag}' else lambda flag: function_name.format(flag=flag)
		)
	
	def render_encoder(self):
		"""Renders the mapping to a string that can be used in a shaderpack's block.properties file"""
		lines = [
			"# The below code was automatically generated by block_wrangler",
			"",
			""
		]
		for entry in self.mapping:
			lines.append(f"# {', '.join(entry['flags'])}")
			lines.append(f"block.{entry['id']} = {entry['blocks'].render()}")
			lines.append("")

		return "\n".join(lines)
	
	def render_decoder(self):
		"""Renders the mapping to GLSL code that can be used to check if a block was in one of the specified categories."""
		lines = [
			f"#if !defined({self.pragma})",
			f"#define {self.pragma}",
			"// This file was automatically generated by block_wrangler",
			"",
			""
		]

		for flag in self.flags:
			if isinstance(flag, str):
				lines.append(f"bool {flag}(int id) {{")
				mapping = {f'id == {entry['id']}' for entry in self.mapping if flag in entry['flags']}
				lines.append(f"\treturn {' || '.join(mapping) if mapping else 'false'};")
				lines.append("}")
			else:
				flag, indices = flag
				
				if any(isinstance(i, float) for i in indices):
					lines.append(f"float {self.function_namer(flag)}(int id) {{")
				else:
					lines.append(f"int {self.function_namer(flag)}(int id) {{")
				for i in indices:
					mapping = {f'id == {entry["id"]}' for entry in self.mapping if f'{flag}.{i}' in entry['flags']}
					if mapping:
						lines.append("\tif (" + ' || '.join(mapping) + ") {")
						lines.append(f"\t\treturn {i};")
						lines.append("\t}")
				lines.append("\treturn 0;")
				lines.append("}")
			lines.append('')
			lines.append('')
		
		for define, value in self.defines.items():
			assert not define.endswith('\\')
			lines.append(f"#define {define} {value}")

		lines.append(f"#endif // {self.pragma}")
		return "\n".join(lines)