from __future__ import annotations
from dataclasses import dataclass, field
import re
from typing import Dict, List, Literal, TypedDict
from rich.progress import Progress, TaskID
from itertools import accumulate, chain

from .block_collections import BlockCollection as _BlockCollection, Blocks as _Blocks
from .config import Configuration
from .progress_sync import ProgressSync

FlagSet = Dict[int, _BlockCollection]|Dict[float, _BlockCollection]|Dict[str, _BlockCollection]

from .flags import IFlag, MapEntry, MappingConfig

FlagValue = int|float|str
FlagEntry = TypedDict('FlagEntry', {'flag':str, 'type':str, 'values':List[FlagValue]})
FlagEntries = List[str|FlagEntry]

@dataclass(frozen=True)
class BlockMapping:
	"""A mapping of block categories to block IDs"""

	mapping:List[MapEntry]
	flags: Dict[str, IFlag]
	config:MappingConfig

	@staticmethod
	def solve(
		flags:Dict[str, IFlag], 
		config:MappingConfig = MappingConfig()
	) -> BlockMapping:
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

		encountered:_BlockCollection = _Blocks({})
		for flag_name in flags.keys():
			if not re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", flag_name):
				raise ValueError(f"Illegal identifier name '{flag_name}'")
		bflags:Dict[str, _BlockCollection] = dict() # Expand any sequence flags into boolean flags
		for name, flag in flags.items():
			bflags |= flag.expand_flags(name)
		
		mapping:Dict[frozenset[str], _BlockCollection] = dict()
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

		return BlockMapping(
			[MapEntry(id=index + config.start_index, flags=key, blocks=val) for index, (key, val) in enumerate(mapping.items())], 
			flags,
			config
		)
	
	def render_encoder(self):
		"""Renders the mapping to a string that can be used in a shaderpack's block.properties file"""
		lines = [
			f"#if !defined({self.config.pragma})",
			f"#define {self.config.pragma}",
			"# The below code was automatically generated by block_wrangler",
			"",
			""
		]
		for entry in self.mapping:
			lines.append(f"# {', '.join(entry['flags'])}")
			lines.append(f"block.{entry['id']} = {entry['blocks'].render()}")
			lines.append("")
		lines.append(f"#endif // {self.config.pragma}")
		return "\n".join(lines)
	
	def render_decoder(self):
		"""Renders the mapping to GLSL code that can be used to check if a block was in one of the specified categories."""
		lines = [
			f"#if !defined({self.config.pragma})",
			f"#define {self.config.pragma}",
			"// This file was automatically generated by block_wrangler",
			"",
			""
		]

		for flag_name, flag in self.flags.items():
			lines.extend(flag.render_decoder(flag_name,self.mapping, self.config))
			lines.append('')
			lines.append('')
		
		for define, value in self.config.defines.items():
			lines.append(f"#define {define} {value}")

		lines.append(f"#endif // {self.config.pragma}")
		return "\n".join(lines)