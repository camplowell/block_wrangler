from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable
from .block_collections import BlockCollection as _BlockCollection, Blocks as _Blocks
from .flags import IFlag, MappingConfig, MapEntry, FlagRenderer

class MappingBuilder:
    def __init__(self, flags: dict[str, IFlag], config: MappingConfig):
        self.flags = {
            k:v.renderer(k)
            for k, v in flags.items()
        }
        self.config = config

    def _solve(self, show_progress: bool = True):
        from itertools import chain
        encountered: _BlockCollection = _Blocks({})
        mapping: dict[frozenset[tuple[str, Any]], _BlockCollection] = dict()
        from functools import reduce
        def flag_tasks(mapping_len: int, flags: FlagRenderer):
            flag_len = len(flags.atomic_flags)
            return mapping_len + flag_len + (mapping_len * flag_len)
        def expected_total(flags: Iterable[FlagRenderer], initial:int=0):
            return reduce(flag_tasks, flags, initial)
        if show_progress:
            try: 
                from rich.progress import Progress
            except ImportError:
                from ._progress_sync import DummyProgress as Progress
            from ._progress_sync import ProgressSync
            flag_values = list(self.flags.values())
        else:
            from ._progress_sync import DummyProgress as Progress
        with Progress(transient=True) as progress:
            if show_progress:
                global_task = progress.add_task(total = expected_total(self.flags.values()), description="Solving flag combinations")
            for index, (flag_name, flag) in enumerate(self.flags.items()):
                subtask = progress.add_task(total=flag_tasks(len(mapping), flag), description=f"{flag_name} ({index + 1} / {len(self.flags)})")
                flag_total = reduce(lambda acc, val: acc + val, flag.atomic_flags.values(), _Blocks({}))
                gen_builder = [[(combo, values.difference, flag_total) for combo, values in mapping.items()]]
                for subflag, subflag_blocks in flag.atomic_flags.items():
                    new_flag = (flag_name, subflag)
                    gen_builder.append([
                        (frozenset([new_flag]), subflag_blocks.difference, encountered)
                    ])
                    gen_builder.append([
                        (frozenset([*combo, new_flag]), values.intersection, subflag_blocks)
                        for combo, values in mapping.items()
                    ])
                generators = chain(*gen_builder)
                if show_progress:
                    generators = ProgressSync(generators, progress, global_task, subtask)
                mapping = {key:val for key, operation, arg in generators if (val := operation(arg))}
                encountered = encountered + flag_total
                if show_progress:
                    progress.remove_task(subtask)
                    if index < len(flag_values):
                        progress.update(global_task, total=expected_total(flag_values[index + 1:], len(mapping)))
        return BlockMapping(
            [MapEntry(id=index + self.config.start_index, flags=key, blocks=val) for index, (key, val) in enumerate(mapping.items())],
            self.flags,
            self.config
        )

    def solve(self, show_progress: bool = True):
        from itertools import chain
        encountered:_BlockCollection = _Blocks({})
        mapping: dict[frozenset[str|tuple[str, Any]], _BlockCollection] = dict()
        from functools import reduce
        if show_progress:
            try:
                from rich.progress import Progress
            except ImportError:
                from ._progress_sync import DummyProgress as Progress
            from ._progress_sync import ProgressSync
            all_flags = list(self.flags.values())
        else:
            from ._progress_sync import DummyProgress as Progress
        with Progress(transient=True) as progress:
            global_task = progress.add_task(total=expected_total(all_flags), description="Solving flag combinations")
            for index, (flag_name, flag) in enumerate(self.flags.items()):
                if show_progress:
                    subtask = progress.add_task(total=flag_tasks(len(mapping), flag), description=f"{flag_name} ({index + 1} / {len(all_flags)})")
                
                # We can skip some intersection checks based on the assertion that a single block cannot have multiple values from the same flag
                flag_blocks = reduce(lambda acc, val: acc + val, flag.atomic_flags.values(), _Blocks({}))
                generators = [[(combo, values.difference, flag_blocks) for combo, values in mapping.items()]]
                for subflag, subflag_blocks in flag.atomic_flags.items():
                    new_flag = flag_name if subflag is True else (flag_name, subflag)
                    generators.append([
                        (frozenset([new_flag]), subflag_blocks.difference, encountered)
                    ])
                    generators.append([
                        (frozenset([*combo, new_flag]), values.intersection, subflag_blocks)
                        for combo, values in mapping.items()
                    ])
                generators = chain(*generators)
                
                if show_progress:
                    generators = ProgressSync(generators, progress, global_task, subtask)
                
                mapping = {key:val for key, operation, arg in generators if bool(val := operation(arg))}
                encountered = encountered.union(flag_blocks)
                
                if show_progress:
                    progress.remove_task(subtask)
                    if index < len(all_flags) - 1:
                        progress.update(global_task, total=expected_total(all_flags[index + 1:], len(mapping)))

        return BlockMapping(
            [MapEntry(id=index + self.config.start_index, flags=key, blocks=val) for index, (key, val) in enumerate(mapping.items())],
            self.flags,
            self.config
        )

def flag_tasks(mapping_len: int, flag: FlagRenderer):
    flag_len = len(flag.atomic_flags)
    return mapping_len + flag_len + (mapping_len * flag_len)

def expected_total(flags: Iterable[FlagRenderer], initial:int=0):
    from functools import reduce
    return reduce(flag_tasks, flags, initial)

@dataclass(frozen=True)
class BlockMapping:
    mapping: list[MapEntry]
    flags: dict[str, FlagRenderer]
    config: MappingConfig

    @staticmethod
    def solve(
        flags: dict[str, IFlag],
        config: MappingConfig = MappingConfig(),
        show_progress: bool = True
    ) -> BlockMapping:
        return MappingBuilder(flags, config).solve(show_progress)
    

    # def render_encoder(self):
    #     """Renders the mapping to a string that can be used in a shaderpack's block.properties file"""
    #     lines = [
    #         "# The below code was automatically generated by block_wrangler",
    #         "",
    #     ]
    #     for entry in self.mapping:
    #         lines.append(f"# {', '.join(entry['flags'])}")
    #         lines.append(f"block.{entry['id']} = {entry['blocks'].render()}")
    #         lines.append("")
    #     return "\n".join(lines)
    
    # def render_decoder(self):
    #     """Renders the mapping to GLSL code that can be used to check if a block was in one of the specified categories."""
    #     lines = [
    #         f"#if !defined({self.config.pragma})",
    #         f"#define {self.config.pragma}",
    #         "// This file was automatically generated by block_wrangler",
    #         "",
    #     ]

    #     for flag_name, flag in self.flags.items():
    #         lines.extend(flag.render_decoder(flag_name,self.mapping, self.config))
    #         lines.append('')
    #         lines.append('')
        
    #     for define, value in self.config.defines.items():
    #         lines.append(f"#define {define} {value}")

    #     lines.append(f"#endif // {self.config.pragma}")
    #     return "\n".join(lines)

