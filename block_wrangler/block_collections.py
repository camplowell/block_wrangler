from __future__ import annotations
from collections import Counter
from itertools import chain
from typing import AbstractSet, Collection, Iterator, Protocol, Dict, Iterable, Set, Tuple, cast, overload, runtime_checkable

from .filters import StateFilter, passthrough
from .block_type import BlockType, BlockState

States = Set[Tuple[int, ...]]

def _filter_states(block:BlockType, filter:StateFilter, * , states:Iterable[Tuple[int, ...]]|None = None) -> States:
	"""Produces a set of states that pass the filter"""
	if states is None:
		states = block.state_tuples()
	return {state for state in states if filter(BlockState(block, state))}

class BlockFamily[T:BlockState](Iterable[BlockType]):
	"""A collection of semantically related block types, optionally with a common signature"""
	_blocks: Iterable[BlockType]
	_signature: type[T]
	def __init__(self, blocks:Iterable[BlockType], / , signature:type[T] = BlockState) -> None:
		self._blocks = (block for block in blocks if block.matches(signature))
		self._signature = signature
	
	def __iter__(self) -> Iterator[BlockType]:
		return iter(self._blocks)
	
	def states(self, filter:StateFilter[T] = passthrough) -> 'BlockCollection[T]':
		return Blocks({block:block.state_tuples() for block in self._blocks}, filter=filter, signature=self._signature, _skip_check=True)

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
		try:
			return Blocks({block:states for block in self.blocks() | other.blocks() if (states := self._get_raw(block, set()) | other._get_raw(block, set()))}, _skip_check=True)
		except TypeError:
			print(f'{type(self).__name__} + {type(other).__name__}')
			raise

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
		block_strs = []
		for block in self.blocks():
			block_strs.extend(str(state) for state in self.get(block))
		
		return f"Blocks({' '.join(block_strs)})"

class Blocks[T:BlockState](BlockCollection[T]):
	"""A collection of concrete block states, optionally with a common signature"""
	_blocks: Dict[BlockType, States]

	def __init__(self, blocks:BlockCollection|Dict[BlockType, Iterable[Tuple[int, ...]]]|Dict[BlockType, States], / , filter:StateFilter[T] = passthrough, * , signature:type[T] = BlockState, _skip_check:bool = False) -> None:
		"""A collection of concrete block states, optionally with a common signature"""
		if isinstance(blocks, BlockCollection):
			blocks = {b:blocks._get_raw(b) for b in blocks.blocks()}
		if _skip_check and filter is passthrough: # Fast path for internal use
			if blocks:
				assert all(isinstance(val, set) for val in blocks.values())
				blocks = cast(Dict[BlockType, States], blocks)
				self._blocks = blocks
				return
		if _skip_check or signature is BlockState:
			get_states = _filter_states
		else:
			def _get_states(block:BlockType, filter:StateFilter[T], states:Iterable[Tuple[int, ...]]) -> States | None:
				if not block.matches(signature):
					return None
				return _filter_states(block, filter, states=states)
			get_states = _get_states
		
		self._blocks = {block:states for block, _states in blocks.items() if (states:=get_states(block, filter, states=_states))}
	
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
	for state_mask, values in zip(range(num_props), block.properties.values()):
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
