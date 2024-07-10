
from typing import Callable, TypeVar
import builtins

from .block_type import BlockState

T = TypeVar('T', bound=BlockState)
StateFilter = Callable[[T], bool]

def passthrough(_:BlockState) -> bool:
	return True

def no(_:BlockState) -> bool:
	return False

def all(*filters:StateFilter) -> StateFilter:
	if no in filters:
		return no
	if builtins.all([f == passthrough for f in filters]):
		return passthrough
	_filters = [f for f in filters if f is not passthrough]
	if len(_filters) == 1:
		return _filters[0]
	def all(state:BlockState) -> bool:
		return builtins.all(filter(state) for filter in filters)
	return all

def any(*filters:StateFilter) -> StateFilter:
	if passthrough in filters:
		return passthrough
	_filters = [f for f in filters if f is not no]
	if len(_filters) == 0:
		return no
	if len(_filters) == 1:
		return _filters[0]
	def any(state:BlockState) -> bool:
		return builtins.any(filter(state) for filter in _filters)
	return any

def none(*filters:StateFilter) -> StateFilter:
	if passthrough in filters:
		return no
	_filters = [f for f in filters if f is not no]
	if len(_filters) == 0:
		return passthrough
	if len(_filters) == 1:
		def not_(state:BlockState) -> bool:
			return not _filters[0](state)
		return not_
	def none(state:BlockState) -> bool:
		return builtins.all(not filter(state) for filter in filters)
	return none