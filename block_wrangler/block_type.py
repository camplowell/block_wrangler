

from dataclasses import dataclass, field
import inspect
from typing import ClassVar, Dict, Final, Literal, Tuple, get_args, get_origin, overload

@dataclass(frozen=True)
class BlockType:
	namespace: str
	name: str
	properties: Dict[str, Tuple[str, ...]] = field(hash=False)

	@property
	def path(self) -> str:
		return self.namespace + ':' + self.name
	
	def matches[T:BlockState](self, signature: type[T]) -> bool:
		return all(name in self.properties and set(self.properties[name]) == set(values) for name, values in signature.typed_properties.items())
	
	def __str__(self) -> str:
		return self.path
	
	def __repr__(self) -> str:
		def prop_str(prop: str, values: Tuple[str, ...]) -> str:
			return f'{prop}=[{", ".join(values)}]'
		return ':'.join([self.namespace, self.name, *(prop_str(prop, values) for prop, values in self.properties.items())])
	
	def __eq__(self, other:object) -> bool:
		if not isinstance(other, BlockType):
			return False
		if self.namespace != other.namespace or self.name != other.name:
			return False
		if self.properties.keys() != other.properties.keys():
			return False
		return all(set(self.properties[name]) == set(other.properties[name]) for name in self.properties.keys())

@dataclass(frozen=True, repr=False, init=False)
class BlockState:
	"""A concrete state of a block type; subclasses may be used to type-hint parts of the state"""
	block:'BlockType'
	_state: Tuple[int, ...] = field(init=False)
	typed_properties: ClassVar[Dict[str, Tuple[str, ...]]] = {}
	MISSING: Final[str] = '\x15'

	def __init__(self, block:'BlockType', state:Tuple[int, ...] | Dict[str, str]) -> None:
		object.__setattr__(self, 'block', block)
		if isinstance(state, dict):
			if state.keys() != block.properties.keys():
				raise ValueError(f"Failed to create state for {block} - given properties {state.keys()} does not match {block.properties.keys()}.")
			object.__setattr__(self, '_state', tuple((block.properties[name].index(state[name]) for name in block.properties.keys())))
		else:
			object.__setattr__(self, '_state', state)

	def __getattr__(self, name: str) -> str:
		if name.startswith('_'):
			raise AttributeError(f"State {self.block.path} has no attribute {name}")
		return self[name]
	
	@overload
	def __getitem__(self, property: str, /) -> str: ...

	@overload
	def __getitem__(self, property: str, / , default: str) -> str: ...

	def __getitem__(self, property: str, / , default=MISSING) -> str:
		i = -1
		for _i, prop in enumerate(self.block.properties.keys()):
			if prop == property:
				i = _i
				break
		if i == -1:
			return default
		return self.block.properties[property][self._state[i]]
	
	def __eq__(self, other:object) -> bool:
		if not isinstance(other, BlockState):
			return False
		if self.block != other.block:
			return False
		return self._state == other._state
	
	def __str__(self) -> str:
		return ':'.join([self.block.path, *(f'{name}={vals[val]}' for (name, vals), val in zip(self.block.properties.items(), self._state))])
	
	def __repr__(self) -> str:
		return str(self)
	
	def __init_subclass__(cls) -> None:
		"""Automatically register properties as part of a block signature"""
		cls_annotations = inspect.get_annotations(cls)
		typed_properties: Dict[str, Tuple[str, ...]] = {}
		for name, type_ in cls_annotations.items():
			if not (get_origin(type_) is Literal and all(isinstance(x, str) for x in get_args(type_))):
				raise TypeError(f'Property {name} must be a literal of strings')
			def make_prop(T:type):
				@property
				def getter(self) -> T:
					return self[name]
				return getter
			setattr(cls, name, make_prop(type_))
			typed_properties[name] = get_args(type_)
		setattr(cls, 'typed_properties', typed_properties)