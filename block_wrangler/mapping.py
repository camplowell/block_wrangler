from dataclasses import dataclass
from typing import Collection, Dict, List, TypeVar, TypedDict
from rich.progress import Progress, TaskID
from itertools import accumulate, chain

from .progress_sync import ProgressSync
from .block_collections import BlockCollection as _BlockCollection, Blocks as _Blocks


def advance(progress:Progress, *tasks:TaskID, advance:int=1):
	for task in tasks:
		progress.update(task, advance=advance)

MapEntry = TypedDict('MapEntry', {'id':int, 'flags':frozenset[str], 'blocks':_BlockCollection})
@dataclass(frozen=True)
class BlockMapping:
	mapping:List[MapEntry]
	flags: List[str]
	pragma:str = "BLOCK_ID_MAPPING"

	@classmethod
	def solve(cls, flags:Dict[str, _BlockCollection], *, start_index:int=1000, pragma:str="BLOCK_ID_MAPPING"):
		mapping:Dict[frozenset[str], _BlockCollection] = dict()
		encountered:_BlockCollection = _Blocks({})
		expected_lengths = [*accumulate(range(len(flags)), lambda x, _: 2 * x + 1, initial=0)]
		with Progress(transient=True) as progress:
			global_task = progress.add_task(total = sum(expected_lengths), description="Solving flag combinations")
			for index, (new_flag, new_values) in enumerate(flags.items()):
				subtask = progress.add_task(total=expected_lengths[index], description=f"Adding {new_flag} ({index + 1} / {len(flags)})")
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
				if index < len(flags) - 1:
					expected_lengths[index + 1:] = [*accumulate(range(len(expected_lengths[index + 1:])), lambda x, _: 2 * x + 1, initial=len(mapping))]
					progress.update(global_task, total=sum(expected_lengths))
		return cls(
			[MapEntry(id=index + start_index, flags=key, blocks=val) for index, (key, val) in enumerate(mapping.items())], 
			list(flags.keys()), 
			pragma
		)
	
	def render_encoder(self):
		lines = [
			"# The below code was automatically generated by block_wrangler",
			"",
			""
		]
		for entry in self.mapping:
			lines.append(f"# {', '.join(entry['flags'])}")
			lines.append(f"block.{entry['id']} = {str(entry['blocks'])}")
			lines.append("")

		return "\n".join(lines)
	
	def render_decoder(self):
		lines = [
			f"#if !defined({self.pragma})",
			f"#define {self.pragma}",
			"// This file was automatically generated by block_wrangler",
			"",
			""
		]

		for flag in self.flags:
			lines.append(f"bool {flag}(int id) {{")
			mapping = {f'id == {entry['id']}' for entry in self.mapping if flag in entry['flags']}
			lines.append(f"\treturn {' || '.join(mapping) if mapping else 'false'};")
			lines.append("}")
			lines.append('')
			lines.append('')

		lines.append(f"#endif // {self.pragma}")
		return "\n".join(lines)