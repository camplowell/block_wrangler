from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import field
from decimal import Decimal
from caseconverter import pascalcase, macrocase
from typing import Any, Callable, Generator, Literal, TypedDict

from block_wrangler.distant_horizons import DHMaterial

from .block_collections import BlockCollection as _BlockCollection, Blocks as _Blocks
from .config import Configuration


MapEntry = TypedDict('MapEntry', {'id':int, 'flags':frozenset[str], 'blocks':_BlockCollection})

class MappingConfig(Configuration):
	"""Configure the way mappings generate code"""

	start_index:int = 1000
	"""The first numerical ID to use for generated block IDs"""

	defines:dict[str, str] = field(default_factory=dict)
	"""Defines to add to the end of the generated code"""

	pragma:str = "BLOCK_ID_MAPPING"
	"""The define used to prevent double-inclusion"""

	id_type:Literal['int', 'uint'] = 'int'


class IFlag(ABC):
	"""Configure the flag within the context of the mapping"""
	@abstractmethod
	def render_decoder(self, flag:str, mapping:list[MapEntry], config:MappingConfig) -> Generator[str, Any, None]: ...
	
	@classmethod
	def check_id(cls, flag:str, mapping:list[MapEntry], dh_materials: DHMaterial):
		possibilities = [f'id == {entry["id"]}' for entry in mapping if flag in entry['flags']]
		possibilities.extend([f'id == {mask.name}' for mask in dh_materials])
		return ' || '.join(possibilities)
	
	@abstractmethod
	def expand_flags(self, flag:str) -> dict[str, _BlockCollection]: ...

class Flag(IFlag):
	class Config(Configuration):
		function_name:Callable[[str], str] = lambda flag: f"Is{pascalcase(flag)}"

		def __call__(self, values:_BlockCollection, dh_materials: DHMaterial = DHMaterial.DH_NONE, **kwargs):
			return Flag(values, dh_materials, config=self | kwargs)
		
	def __init__(self, values:_BlockCollection, dh_materials: DHMaterial = DHMaterial.DH_NONE, * , config:Configuration = Config()):
		self.values = values
		self.config = self.Config() | config
		self.dh_materials = dh_materials


	def function_decl(self, return_type:str, flag:str, config:MappingConfig) -> str:
		function_name = self.config.function_name(flag)
		return f"{return_type} {function_name}({config.id_type} id) {{"
	
	def render_decoder(self, flag:str, mapping:list[MapEntry], config:MappingConfig):
		yield self.function_decl('bool', flag, config)
		yield f"\treturn {self.check_id(flag, mapping, self.dh_materials)};"
		yield "}"

	def expand_flags(self, flag:str) -> dict[str, _BlockCollection]:
		return {flag:self.values}

class FlagSequence[T](IFlag, ABC):
	class Config(Configuration):
		function_name:Callable[[str], str] = lambda flag: f"Get{pascalcase(flag)}"
		"""The name of the function to retrieve the type of a sequence flag"""
	
	def __init__(self, contents:dict[T, _BlockCollection|tuple[_BlockCollection, DHMaterial]], default:T, * , config:Config|None = None):
		if config is None:
			config = self.__class__.Config()
		self.contents = {k:v[0] if isinstance(v, tuple) else _Blocks(v) for k, v in contents.items()}
		self.dh_materials = {k:v[1] if isinstance(v, tuple) else DHMaterial.DH_NONE for k, v in contents.items()}
		self.default = default
		self.config = self.Config() | config

	def render_value(self, value:T) -> str: return str(value)
	"""Express the value of a flag in GLSL"""
	def decoder_prefix(self) -> Generator[str, Any, None]: yield from []
	"""Any code that should appear before the decoder function"""
	def decoder_suffix(self) -> Generator[str, Any, None]: yield from []
	"""Any code that should appear after the decoder function"""

	def subflag(self, flag:str, i:int, value:T):
		"""The name of the boolean flag for a given value. Defaults to the value's index."""
		return f'{flag}.{i}'

	@property
	def return_type(self) -> str: ...
	"""The return type of the decoder function"""

	def function_decl(self, return_type:str, flag:str, config:MappingConfig) -> str:
		function_name = self.config.function_name(flag)
		return f"{return_type} {function_name}({config.id_type} id) {{"

	def render_decoder(self, parent_flag:str, mapping: list[MapEntry], config:MappingConfig) -> Generator[str, Any, None]:
		setattr(self, 'flag', parent_flag)
		setattr(self, 'global_config', config)
		yield from self.decoder_prefix()
		yield self.function_decl(self.return_type, parent_flag, config)
		for i, value in enumerate(self.contents.keys()):
			flag = self.subflag(parent_flag, i, value)
			dh_materials = self.dh_materials[value]
			yield f"\tif ({self.check_id(flag, mapping, dh_materials)})"
			yield f"\t\treturn {self.render_value(value, )};"
		yield f"\treturn {self.render_value(self.default, )};"
		yield "}"
		yield from self.decoder_suffix()
		delattr(self, 'flag')
		delattr(self, 'config')
	
	def expand_flags(self, flag:str) -> dict[str, _BlockCollection]:
		seen = _Blocks({})
		bool_flags:dict[str, _BlockCollection] = dict()
		for i, (key, value) in enumerate(self.contents.items()):
			overlap = seen & value
			if overlap:
				raise ValueError(f"{flag} has an ambiguous value for the following blocks: {overlap}")
			bool_flags[self.subflag(flag, i, key)] = value
			seen += value
		return bool_flags

class IntFlag(FlagSequence[int]):
	class Config(FlagSequence.Config):
		def __call__(self, contents:dict[int, _BlockCollection|tuple[_BlockCollection, DHMaterial]], default:int=0, **kwargs):
			return IntFlag(contents, default, config=self | kwargs)
	
	@property
	def return_type(self) -> str: return 'int'

class FloatFlag(FlagSequence[float|Decimal]):
	class Config(FlagSequence.Config):
		def __call__(self, contents:dict[float|Decimal, _BlockCollection|tuple[_BlockCollection, DHMaterial]], default:float|Decimal=0.0, **kwargs):
			return FloatFlag(contents, default, config=self | kwargs)
	@property
	def return_type(self) -> str: return 'float'

class EnumFlag(FlagSequence[str]):
	class Config(FlagSequence.Config):
		enum_name:Callable[[str], str] = lambda flag: pascalcase(flag)
		"""The name of the enum type to use for enum-like flags"""

		enum_value_name:Callable[[str, str], str] = lambda flag, value: f'{pascalcase(flag)}_{macrocase(value)}'
		"""The name of the enum value to use for enum-like flags"""

		type_safety:bool = True
		"""Use a struct to ensure type safety; requires #version 130 or higher"""

		def __call__(self, contents:dict[str, _BlockCollection | tuple[_BlockCollection, DHMaterial]], default:str = 'NONE', **kwargs):
			return EnumFlag(contents, default, config=self | kwargs)
		
	config: Config
	
	@property
	def return_type(self) -> str: 
		if self.config.type_safety:
			return self.config.enum_name(self.flag)
		else:
			return 'int'
	
	def _value_name(self, value:str) -> str:
		return self.config.enum_value_name(self.flag, value)
	
	def render_value(self, value:str) -> str:
		return f"{self._value_name(value)}"
	
	def decoder_prefix(self) -> Generator[str, Any, None]:
		if self.config.type_safety:
			yield f"struct {self.return_type} {{int value;}};"
		def declare_val(value:str, i:int):
			if self.config.type_safety:
				return f"const {self.return_type} {self._value_name(value)} = {self.return_type}({i});"
			else:
				return f"const {self.return_type} {self._value_name(value)} = {i};"
		yield declare_val(self.default, 0)
		for i, value in enumerate(self.contents.keys()):
			yield declare_val(value, i + 1)
	
	def render_decoder(self, parent_flag: str, mapping: list[MapEntry], config: MappingConfig) -> Generator[str, Any, None]:
		self.flag = parent_flag
		self.gloabl_config = config
		return super().render_decoder(parent_flag, mapping, config)
