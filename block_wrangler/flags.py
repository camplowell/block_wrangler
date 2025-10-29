from __future__ import annotations
from abc import ABC, abstractmethod
from caseconverter import pascalcase, camelcase, macrocase
from dataclasses import dataclass, field
from typing import Any, Callable, Generator, Literal, TypedDict, Unpack

from .block_collections import BlockCollection as _BlockCollection, Blocks as _Blocks
from .config import Configuration
from .distant_horizons import DHMaterial

class BaseTypedDict(TypedDict, total=False): pass

class IFlag[C: BaseTypedDict](ABC):
	def __init__(self, config: C):
		self.config = type(self).config | config
	config: C

	@abstractmethod
	def renderer(self, name: str) -> FlagRenderer: ...

class FlagRenderer[T](ABC):
	@abstractmethod
	def render_decoder(self, values: dict[T, list[int]], config: MappingConfig) -> Generator[str, Any, None]: ...

	atomic_flags: dict[T, _BlockCollection]
	"""The individual block collections for each value"""

	@staticmethod
	def id_check(ids: list[int], dh_materials: DHMaterial):
		return ' || '.join(f'id == {i}' for i in [
			*[str(i) for i in ids],
			*[mask.name for mask in dh_materials]
		])

class FlagConfig(TypedDict, total=False):
	function_name: Callable[[str], str]
	"""The name of the GLSL decoder function"""

class Flag(IFlag[FlagConfig]):
	def __init__(
		self,
		values: _BlockCollection,
		materials: DHMaterial = DHMaterial.DH_NONE,
		**kwargs: Unpack[FlagConfig]
	):
		"""A Flag with a boolean value.

		Args:
			values (BlockCollection): Which blocks should match the flag
			materials (DHMaterial): Which Distant Horizons materials should match the flag
			function_name (Callable[[str], str], optional): The name of the GLSL decoder function
		"""
		super().__init__(kwargs)
		self.values = values
		self.materials = materials
	config: FlagConfig = {
		'function_name': lambda s: f"is{pascalcase(s)}"
	}
	
	def renderer(self, name: str):
		return BoolFlagRenderer(
			fn_name=self.config.get('function_name', lambda flag: f"is{pascalcase(flag)}")(name),
			blocks=self.values,
			dh_materials=self.materials
		)
	
	@classmethod
	def Config(cls, **defaults: Unpack[FlagConfig]):
		"""Create an alternate constructor with different default values
		Args:
			default_value (int, optional): The default value for non-matches
			function_name (Callable[[str], str], optional): The name of the GLSL decoder function
		"""
		def create(
				values: _BlockCollection,
				materials: DHMaterial = DHMaterial.DH_NONE,
				**kwargs: Unpack[SequenceConfig[int]]):
			return cls(values, materials, **(defaults | kwargs))
		return create

type FlagMapping[T] = dict[T, _BlockCollection|tuple[_BlockCollection, DHMaterial]]

class SequenceConfig[T](FlagConfig, total=False):
	default_value: T

class FlagSequence[T, C: SequenceConfig](IFlag[C]):
	def __init__(self, values: FlagMapping[T], config: C):
		self.values = values
		sequence_full = _Blocks({})
		for key, blocks in values.items():
			if isinstance(blocks, tuple): blocks = blocks[0]
			next_full = sequence_full.union(blocks)
			if len(next_full) < len(sequence_full) + len(blocks):
				raise ValueError(f"Flag value {self.display_value(key)} has blocks seen in a previous value:\n{sequence_full.intersection(blocks).render()}")
			sequence_full = next_full
		super().__init__(config)
	
	@classmethod
	def Config(cls, **defaults: Unpack[SequenceConfig[T]]):
		"""Create an alternate constructor with different default values
		Args:
			default_value (int, optional): The default value for non-matches
			function_name (Callable[[str], str], optional): The name of the GLSL decoder function
		"""
		def create(values: FlagMapping[int], **kwargs: Unpack[SequenceConfig[int]]):
			return cls(values, **(defaults | kwargs))
		return create

	def value_name(self, val: T, flag: str) -> str: return str(val)
	def display_value(self, val: T) -> str: return str(val)

	def return_type(self, flag: str) -> str: ...

	def fn_prefix(self, flag: str) -> str|None: return None

	def fn_suffix(self, flag: str) -> str|None: return None

	def renderer(self, flag: str):
		assert 'function_name' in self.config
		assert 'default_value' in self.config
		fn_name = self.config['function_name'](flag)
		import re
		if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', fn_name):
			raise ValueError(f"Invalid function name: '{fn_name}'")
		return MultiFlagRenderer(
			atomic_flags={
				k:v[0] if isinstance(v, tuple) else v
				for k, v in self.values.items()
			},
			value_info={
				k:ValueInfo(
					v[1] if isinstance(v, tuple) else DHMaterial.DH_NONE,
					glsl_value=self.value_name(k, flag),
					display_value=self.display_value(k)
				)
				for k,v in self.values.items()
            },
			default_value=self.value_name(self.config['default_value'], flag),
			fn_decl=f'{self.return_type(flag)} {fn_name}',
			fn_prefix=self.fn_prefix(flag),
			fn_suffix=self.fn_suffix(flag)
		)

class IntFlag(FlagSequence[int, SequenceConfig[int]]):
	def __init__(
		self, 
		values: FlagMapping[int], 
		**kwargs: Unpack[SequenceConfig[int]]
	):
		"""A Flag with integer values

		Args:
			values (FlagMapping[int]): A mapping from values to block states (and Distant Horizons materials)
			default_value (int, optional): The default value for non-matches
			function_name (Callable[[str], str], optional): The name of the GLSL decoder function
		"""
		super().__init__(values, kwargs)

	config: SequenceConfig[int] = {
		'function_name': lambda name: camelcase(name),
		'default_value': 0
	}
	
	def return_type(self, flag: str): return 'int'

	@classmethod
	def Config(cls, **defaults: Unpack[SequenceConfig[int]]):
		"""Create an alternate constructor with different default values
		Args:
			default_value (int, optional): The default value for non-matches
			function_name (Callable[[str], str], optional): The name of the GLSL decoder function
		"""
		def create(values: FlagMapping[int], **kwargs: Unpack[SequenceConfig[int]]):
			return cls(values, **(defaults | kwargs))
		return create

class FloatFlagConfig(SequenceConfig[float], total=False):
	format: Callable[[float], str]

class FloatFlag(FlagSequence[float, FloatFlagConfig]):
	def __init__(
		self, 
		values: FlagMapping[float], 
		**kwargs: Unpack[FloatFlagConfig]
	):
		"""A Flag with float values

		Args:
			values (FlagMapping[float]): A mapping from values to block states (and Distant Horizons materials)
			default_value (float, optional): The default value for non-matches
			function_name (Callable[[str], str], optional): The name of the GLSL decoder function
			format (Callable[[float], str], optional): How to display values in the settings screen
		"""
		super().__init__(values, kwargs)

	config: FloatFlagConfig = {
		'function_name': lambda name: camelcase(name),
		'format': lambda val: f'{val:.2f}',
		'default_value': 0.0
	}

	def return_type(self, flag: str): return 'float'

	def display_value(self, val: float) -> str:
		assert 'format' in self.config
		return self.config['format'](val)

	@classmethod
	def Config(cls, **defaults: Unpack[FloatFlagConfig]):
		"""Create an alternate constructor with different default values
		Args:
			default_value (float, optional): The default value for non-matches
			function_name (Callable[[str], str], optional): The name of the GLSL decoder function
			format (Callable[[float], str], optional): How to display values in the settings screen
		"""
		def create(values: FlagMapping[float], **kwargs: Unpack[FloatFlagConfig]):
			return cls(values, **(defaults | kwargs))
		return create

class EnumFlagConfig(SequenceConfig[str], total=False):
	enum_name: Callable[[str], str]|None
	enum_value_name: Callable[[str, str], str]
	"""Use a struct to ensure type safety; requires #version 130 or higher"""

class EnumFlag(FlagSequence[str, EnumFlagConfig]):
	def __init__(self, values: FlagMapping[str], **config: Unpack[EnumFlagConfig]):
		"""A Flag with enumerated values

		Args:
			values (FlagMapping[str]): A mapping from values to block states (and Distant Horizons materials)
			default_value (str, optional): The default value for non-matches
			function_name (Callable[[str], str], optional): The name of the GLSL decoder function
			enum_name (Callable[[str], str], optional): The name of the enum struct used for type safety (requires #version 130 or higher)
			enum_value_name (Callable[[str, str], str], optional): The macro names for the enumerated values
		"""
		super().__init__(values, config)
	
	config: EnumFlagConfig = {
		'function_name': lambda x: camelcase(x),
		'default_value': 'NONE',
		'enum_name': lambda flag: pascalcase(flag),
		'enum_value_name': lambda flag, value: f'{pascalcase(flag)}_{macrocase(value)}'
	}

	def return_type(self, flag: str):
		if name_fn := self.config.get('enum_name'):
			return name_fn(flag)
		return 'int'
	
	def display_value(self, val: str) -> str: return val

	def fn_prefix(self, flag: str) -> str:
		from caseconverter import pascalcase, macrocase
		sname = pascalcase(flag)
		return '\n'.join([
			f"struct {sname}Values {{",
			f"\tint {self.config['default_value']}",
			*[f"\tint {macrocase(name)};" for name in self.values.keys()],
			"};",
			f"const {sname}Values {sname} = {sname}Values({', '.join(str(i) for i in range(len(self.values) + 1))})"
		])
	
	def value_name(self, val: str, flag: str):
		from caseconverter import pascalcase, macrocase
		return f"{pascalcase(flag)}.{macrocase(val)}"

	@classmethod
	def Config(cls, **defaults: Unpack[EnumFlagConfig]):
		"""Create an alternate constructor with different default values
		Args:
			default_value (str, optional): The default value for non-matches
			function_name (Callable[[str], str], optional): The name of the GLSL decoder function
			enum_name (Callable[[str], str], optional): The name of the enum struct used for type safety (requires #version 130 or higher)
			enum_value_name (Callable[[str, str], str], optional): The macro names for the enumerated values
		"""
		def create(values: FlagMapping[str], **kwargs: Unpack[EnumFlagConfig]):
			return cls(values, **(defaults | kwargs))
		return create


class BoolFlagRenderer(FlagRenderer[bool]):
	def __init__(self, fn_name: str, blocks: _BlockCollection, dh_materials: DHMaterial):
		import re
		if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', fn_name):
			raise ValueError(f"Invalid identifier name: '{fn_name}'")
		self.fn_name = fn_name
		self.dh_materials = dh_materials
		self.atomic_flags = {True:blocks}
	
	def render_decoder(self, values: dict[bool, list[int]], config: MappingConfig) -> Generator[str, Any, None]:
		yield f"bool {self.fn_name}({config.id_type} id) {{"
		if check := self.id_check(values[True], self.dh_materials):
			yield f"    return {check};"
		else:
			yield "    return false;"
		yield "}"

@dataclass
class ValueInfo:
	materials: DHMaterial = DHMaterial.DH_NONE
	glsl_value: str = field(kw_only=True)
	display_value: str = field(kw_only=True)

@dataclass
class MultiFlagRenderer[T](FlagRenderer[T]):
	atomic_flags: dict[T, _BlockCollection]
	"""The individual block collections for each value"""
	value_info: dict[T, ValueInfo]
	fn_decl: str
	default_value: str
	"""The function declaration (ex: `int emissivity`)"""
	fn_prefix: str|None = None
	fn_suffix: str|None = None

	def render_decoder(self, values: dict[T, list[int]], config: MappingConfig) -> Generator[str, Any, None]:
		if self.fn_prefix: yield self.fn_prefix
		yield f"{self.fn_decl}({config.id_type} id) {{"
		first = True
		for val, ids in values.items():
			info = self.value_info[val]
			if check := self.id_check(ids, info.materials):
				yield f"    {'if' if first else '} else if'} ({check}) {{"
				yield f"        return {info.glsl_value};"
				first = False
		if first:
			yield f'    return {self.default_value};'
		else:
			yield "    } else {"
			yield f"        return {self.default_value};"
			yield '    }'
		yield '}'
		if self.fn_suffix: yield self.fn_suffix
		

class MappingConfig(Configuration):
	"""Configure the way mappings generate code"""

	start_index:int = 1000
	"""The first numerical ID to use for generated block IDs"""

	defines:dict[str, str] = field(default_factory=dict)
	"""Defines to add to the end of the generated code"""

	pragma:str = "BLOCK_ID_MAPPING"
	"""The define used to prevent double-inclusion"""

	id_type:Literal['int', 'uint'] = 'int'

	def __post_init__(self):
		from ._rich_log import getLogger
		logger = getLogger()
		if self.start_index < 16:
			logger.warning("Block ID start index should be 16 or more to avoid collisions with DH material IDs")

