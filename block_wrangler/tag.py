from dataclasses import dataclass, field
from typing import Collection, Dict, Iterable, List, Self, Tuple

from .block_collections import Blocks, _filter_states
from .block_type import BlockState, BlockType
from . import filters
from .filters import StateFilter

@dataclass
class Tag:
	"""A structure that produces a collection of block (states) that are semantically related to each other"""
	name: str
	parent: Self | None
	sources: Dict[Self, StateFilter] = field(default_factory=dict, init=False)
	_filters: Dict[BlockType, StateFilter] = field(default_factory=dict, init=False)
	@dataclass
	class WidenedMode:
		"""The tag will filter all blocks from its parent"""
		filter: StateFilter

	@dataclass
	class NarrowedMode:
		"""The tag will only contain blocks in its source tags (ex: children)"""
		strict: bool

	@dataclass
	class DefaultMode:
		"""The tag will contain blocks from its source tags and any blocks it has an explicit filter for"""
		pass

	TagMode = DefaultMode | NarrowedMode | WidenedMode
	mode: TagMode = field(default_factory=DefaultMode, init=False)

	def __post_init__(self) -> None:
		if self.parent is not None:
			self.parent.add(self)
	
	def add[T:BlockState](self, source: Self|Iterable[BlockType], filter:StateFilter[T] = filters.passthrough) -> Self:
		"""Add a collection of blocks to the tag, and optionally a filter to apply to their states"""
		if isinstance(source, Tag):
			source._validate_source([self])
			self.sources[source] = filter
			return self
		for block in source:
			if block in self._filters:
				self._filters[block] = filters.any(filter, self._filters[block])
			else:
				self._filters[block] = filter
		return self
	
	def set_mode(self, mode:TagMode) -> Self:
		"""Define the behavior of the tag in relation to other tags"""
		old_mode, self.mode = self.mode, mode
		self.mode = mode
		try:
			self._validate_source([])
		except:
			self.mode = old_mode # roll back in case of error
			raise
		return self
	
	def resolve(self) -> Blocks:
		"""Resolve the tag to a concrete Blocks collection"""
		block_states = dict()
		for block, upstream in self._upstream_filters().items():
			filtered = _filter_states(block, filters.all(upstream, self._downstream_filter(block)))
			if filtered:
				block_states[block] = filtered
		return Blocks(block_states)

	def _validate_source(self, seen:List[Self]) -> None:
		if isinstance(self.mode, Tag.WidenedMode) and self.parent in seen:
			return # prevent infinite recursion when using widened mode
		if self in seen:
			raise RecursionError(f"Circular dependency detected: {' -> '.join([tag.name for tag in seen])} -> {self.name}")
		seen.append(self)
		for source in self.sources.keys():
			source._validate_source(seen)
		seen.pop()
	
	def _upstream_tags(self) -> Iterable[Tuple[Self, StateFilter]]:
		if isinstance(self.mode, Tag.WidenedMode):
			return self.sources.items() | (set([(self.parent, self.mode.filter)]) if self.parent else set())
		return self.sources.items()

	def _downstream_filter(self, block:BlockType) -> StateFilter:
		my_filter = self._filters.get(block, filters.passthrough)
		if self.parent:
			return filters.all(my_filter, self.parent._downstream_filter(block))
		return my_filter
	

	def _upstream_filters(self, seen:List[Self] = []) -> Dict[BlockType, StateFilter]:
		if isinstance(self.mode, Tag.WidenedMode) and self.parent in seen:
			return dict() # prevent infinite recursion when using widened mode
		if self in seen:
			raise RecursionError(f"Circular dependency detected: {' -> '.join([tag.name for tag in seen])} -> {self.name}")
		seen.append(self)

		upstream_blocks:Dict[BlockType, StateFilter] = dict()
		for source, source_filter in self._upstream_tags():
			for block, filter in source._upstream_filters(seen).items():
				if block in upstream_blocks:
					upstream_blocks[block] = filters.any(upstream_blocks[block], filters.all(source_filter, filter))
				else:
					upstream_blocks[block] = filters.all(source_filter, filter)
		seen.pop()

		for block, filter in self._filters.items():
			if block in upstream_blocks:
				if isinstance(self.mode, Tag.NarrowedMode):
					upstream_blocks[block] = filters.all(upstream_blocks[block], filter)
				else:
					upstream_blocks[block] = filters.any(upstream_blocks[block], filter)
			elif not (isinstance(self.mode, Tag.NarrowedMode) and self.mode.strict):
					upstream_blocks[block] = filter
		
		return {block:filter for block, filter in upstream_blocks.items() if filter is not filters.no}
	
	def __hash__(self) -> int:
		return hash(self.name)
	
	def __eq__(self, other:object) -> bool:
		return id(self) == id(other) # use the id to enforce singleton-like behavior

	def __str__(self) -> str:
		return self.name
	
	def __repr__(self) -> str:
		return f"Tag({self.name})"

try:
	import rapidfuzz as fuzz
except ImportError:
	fuzz = None

class TagLibrary:
	"""A library of tags"""
	def __init__(self) -> None:
		self.tags:Dict[str, Tag] = dict()
	
	def touch(self, tag:str) -> Tag:
		"""Ensure that the tag exists in the library and return it"""
		if tag not in self.tags:
			self.tags[tag] = Tag(tag, self.touch(tag[:tag.rindex('/')]) if '/' in tag else None)
		return self.tags[tag]
	
	def tag_progressive(self, blocks:Iterable[BlockType], parent: str, tags: Collection[str|int], property: str,  values: Collection[str|int], filter:StateFilter=filters.passthrough) -> None:
		"""Add a sequence of block states to a sequence of tags"""
		if len(tags) != len(values):
			raise ValueError(f"Tags and values must be the same length")
		for tag, value in zip(tags, values):
			self.touch(parent + '/' + str(tag)).add(blocks, lambda state: state[property] == str(value))
	
	def __getitem__(self, tag:str) -> Blocks:
		"""Resolve the tag to a Blocks collection"""
		if tag not in self.tags:
			if fuzz is None:
				raise KeyError(f"Tag {tag} not found")
			best_match, similarity, _ = fuzz.process.extractOne(tag, self.tags.keys(), scorer=fuzz.distance.Levenshtein.distance)
			
			if similarity > 5:
				raise KeyError(f"Tag {tag} not found (no similar tags found)")
			raise KeyError(f"Tag {tag} not found, did you mean {best_match}? ({similarity})")
		return self.tags[tag].resolve()
			
				
	
	def __len__(self) -> int:
		return len(self.tags)