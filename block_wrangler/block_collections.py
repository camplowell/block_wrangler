from collections import Counter
from itertools import product, chain
from typing import AbstractSet, Collection, Iterator, Protocol, Dict, Iterable, Set, Tuple, cast, overload, runtime_checkable

from .filters import StateFilter, passthrough
from .block_type import BlockType, BlockState

States = Set[Tuple[int, ...]]

def _filter_states(block:BlockType, filter:StateFilter, * , states:Iterable[Tuple[int, ...]]|None = None) -> States:
	"""Produces a set of states that pass the filter"""
	if states is None:
		if block.properties:
			states = product(*[range(len(vals)) for vals in block.properties.values()])
		else:
			states = [tuple()]
	result = set()
	for state in states:
		if filter(BlockState(block, state)):
			result.add(state)
	return result


class BlockFamily[T:BlockState](Iterable[BlockType]):
	"""A collection of semantically related block types, optionally with a common signature"""
	_blocks: Iterable[BlockType]
	def __init__(self, blocks:Iterable[BlockType], / , signature:type[T] = BlockState) -> None:
		self._blocks = (block for block in blocks if block.matches(signature))
	
	def __iter__(self) -> Iterator[BlockType]:
		return iter(self._blocks)

@runtime_checkable
class BlockCollection[T:BlockState](Collection[T], Protocol):
	"""A collection of concrete block states, optionally with a common signature"""
	def blocks(self) -> AbstractSet[BlockType]: ...

	def _get_raw(self, block:BlockType, / , default:States=set()) -> States: ...

	@overload 
	def get(self, block:BlockType, /) -> Iterable[T]: ...

	@overload
	def get[D](self, block:BlockType, / , default:Iterable[D]) -> Iterable[T|D]: ...

	def get[D](self, block:BlockType, / , default:Iterable[D]=...) -> Iterable[T|D]:
		"""Get the block state for the given block, or the default value if the block is not in this collection"""
		if block in self.blocks():
			return (cast(T,BlockState(block,raw)) for raw in self._get_raw(block))
		elif default is ...:
			raise KeyError(block)
		return default
	
	def render(self) -> str:
		return ' '.join(_render_block(block, self._get_raw(block)) for block in self.blocks())


	def union(self, other:'BlockCollection') -> 'BlockCollection': 
		"""Create a new BlockCollection that contains all the blocks in this collection and the other collection"""
		return Blocks({block:states for block in self.blocks() | other.blocks() if (states := self._get_raw(block, set()) | other._get_raw(block, set()))}, _skip_check=True)

	def difference(self, other:'BlockCollection') -> 'BlockCollection':
		"""Create a new BlockCollection that contains all the blocks in this collection but not the other collection"""
		return Blocks({block:states for block in self.blocks() if (states := self._get_raw(block) - other._get_raw(block, set()))}, _skip_check=True)

	def intersection(self, other:'BlockCollection') -> 'BlockCollection': 
		"""Create a new BlockCollection that contains all the blocks in this collection and the other collection"""
		return Blocks({block:states for block in self.blocks() & other.blocks() if (states := self._get_raw(block) & other._get_raw(block))}, _skip_check=True)

	def where(self, filter:StateFilter[T]) -> 'BlockCollection': 
		"""Create a new Blocks collection that contains only the blocks that pass the filter"""
		return Blocks({block:states for block in self.blocks() if (states := _filter_states(block, filter))}, _skip_check=True)
	
	def __iter__(self) -> Iterable[T]:
		return chain(*(self.get(block) for block in self.blocks()))
	
	def __len__(self):
		return sum(len(self._get_raw(block)) for block in self.blocks())

	def __contains__(self, element:BlockType|BlockState) -> bool: 
		if isinstance(element, BlockState):
			return element.block in self.blocks() and element._state in self._get_raw(element.block)
		return element in self.blocks()
	
	def __add__(self, other:'BlockCollection') -> 'BlockCollection':
		return self.union(other)
	
	def __sub__(self, other:'BlockCollection') -> 'BlockCollection':
		return self.difference(other)
	
	def __and__(self, other:'BlockCollection') -> 'BlockCollection':
		return self.intersection(other)
	
	def __str__(self):
		return self.render()
	
	def __repr__(self):
		return f"Blocks({self.render()})"

class Blocks[T:BlockState](BlockCollection[T]):
	"""A collection of concrete block states, optionally with a common signature"""
	_blocks: Dict[BlockType, States]
	def __init__(self, blocks:BlockFamily[T]|Iterable[BlockType]|Dict[BlockType, States], / , filter:StateFilter[T] = passthrough, * , signature:type[T] = BlockState, _skip_check:bool = False) -> None:
		"""A collection of concrete block states, optionally with a common signature
		Args:
			blocks (Iterable[BlockType]|Dict[BlockType, States]): the block(states) to consider
			filter (StateFilter[T], optional): Discards any block states that don't pass the filter.
			signature (type[T], optional): Discards any blocks that don't match the signature and provides type hints for the filter.
		"""
		if isinstance(blocks, dict):
			if _skip_check or signature is BlockState:
				self._blocks = blocks.copy()
				return
			if filter is passthrough:
				self._blocks = {block:states for block, states in blocks.items() if block.matches(signature)}
			else:
				def _filter(block:BlockType, states:States) -> States:
					if not block.matches(signature):
						return set()
					return {state for state in states if filter(cast(T, BlockState(block, state)))}
				self._blocks = {block:filtered for block, unfiltered in blocks.items() if (filtered:=_filter(block, unfiltered))}
			self._blocks = blocks.copy()
		else:
			self._blocks = {block:states for block in blocks if block.matches(signature) and (states:=_filter_states(block, filter))}
	
	def blocks(self) -> AbstractSet[BlockType]:
		return self._blocks.keys()

	def _get_raw(self, block:BlockType, / , default:States=set()) -> States:
		return self._blocks.get(block, default)
	
	def __eq__(self, other:object) -> bool:
		if not isinstance(other, Blocks):
			return False
		return self._blocks == other._blocks

def _render_block(block:BlockType, states:States) -> str:
	num_props = len(block.properties)
	for i, value in enumerate(block.properties.values()):
		assert all(state[i] < len(value) for state in states)
	if num_props == 0:
		return block.path
	for state_mask, (key, values) in zip(range(num_props), block.properties.items()):
		state_counter:Counter[Tuple[int, ...]] = Counter()
		for state in states:
			state_counter[_mask_property(state, state_mask)] += 1
		num_values = len(values)
		for masked_state, count in state_counter.items():
			assert count <= num_values
			if count < num_values:
				continue
			prev_len = len(states)
			states = {state for state in states if _mask_property(state, state_mask) != masked_state}
			assert len(states) == prev_len - count
			states.add(masked_state)
	return ' '.join(_render_state(block, state) for state in states)

def _mask_property(state:Tuple[int, ...], mask:int):
	return tuple([-1 if i == mask else val for i, val in enumerate(state)])

def _render_state(block:BlockType, state:Tuple[int, ...]) -> str:
	return ':'.join([block.path, *(f'{name}={vals[val]}' for (name, vals), val in zip(block.properties.items(), state) if val != -1)])