from pkgutil import iter_modules as _iter_modules, walk_packages as _walk_packages
import typing as _tp
from functools import cache as _cache, reduce as _reduce
from importlib import import_module as _import_module
from itertools import chain as _chain

from block_wrangler.tag import TagLibrary as _TagLibrary
from block_wrangler.block_type import BlockType as _BlockType, BlockState as _BlockState
from block_wrangler.block_collections import Blocks as _Blocks, BlockCollection as _BlockCollection, BlockFamily as _BlockFamily
from block_wrangler._rich_log import getLogger as _getLogger
from block_wrangler.filters import StateFilter as _StateFilter, passthrough as _passthrough
from block_wrangler import filters as _filters

from . import blocks as _blocks, tags as _tags

_log = _getLogger(__name__)

def load_tags() -> _TagLibrary:
	"""Returns a TagLibrary containing a collection of Vanilla and other common tags"""
	_log.verbose('Loading tags')
	result = _TagLibrary()
	for module_name in (module.name for module in _walk_packages(_tags.__path__, f"{_tags.__name__}.")):
		module = _import_module(module_name)
		if hasattr(module, 'load_tags'):
			module.load_tags(result)
	return result

def blocks(*blocks:str|_BlockType, strict:bool=True) -> _BlockCollection:
	"""Create a Blocks collection from the given blocks"""
	return _reduce(lambda acc, block: acc.union(block), (block for block_str in blocks if (block := _coerce_block(block_str, strict=strict)) is not None), _Blocks(dict()))

def gather_blocks[T:_BlockState](condition:_tp.Callable[[_BlockType], bool] = _passthrough, signature:_tp.Type[T]=_BlockState, filter:_StateFilter=_filters.passthrough) -> _Blocks[T]:
	"""Find all blocks that match the condition and return them as a Blocks collection"""
	return _Blocks((block for block in _all_blocks() if condition(block)), filter=filter, signature=signature)

def block_types(*blocks:str|_BlockType , strict:bool=True) -> _tp.Iterable[_BlockType]:
	return (block for block_str in blocks if (block := _coerce_block_type(block_str, strict=strict)) is not None)

def gather_block_types[T:_BlockState](condition:_tp.Callable[[_BlockType], bool] = _passthrough, signature:_tp.Type[T]=_BlockState) -> _BlockFamily[T]:
	"""Find all block types that match the condition and return them"""
	return _BlockFamily((block for block in _all_blocks() if condition(block)), signature=signature)


@_cache
def _all_blocks() -> _tp.Iterable[_BlockType]:
	return _chain(*(_block_namespace(namespace).values() for namespace in _iter_modules(_blocks.__path__)))

@_cache
def _block_namespace(namespace:str, strict:bool=True) -> _tp.Dict[str, _BlockType]:
	try:
		namespace_module = _import_module(f'.{namespace}', _blocks.__name__)
	except ModuleNotFoundError as e:
		if strict:
			raise e
		return {}
	return { var.name:var for var in namespace_module.__dict__.values() if isinstance(var, _BlockType) }

def _coerce_block_type(raw:str|_BlockType, strict:bool=True) -> _BlockType | None:
	if isinstance(raw, _BlockType):
		return raw
	assert '=' not in raw
	if ':' in raw:
		namespace, name = raw.split(':', 1)
	else:
		namespace, name = 'minecraft', raw
	try:
		return _block_namespace(namespace, strict=strict)[name]
	except KeyError:
		if strict:
			raise
		return None

def _coerce_block(raw:str|_BlockType, strict:bool=True) -> _Blocks | None:
	if isinstance(raw, _BlockType):
		return _Blocks([raw])
	if '=' not in raw:
		name_part = raw
		params_part = []
	else:
		split_index = raw.rindex(':', 0, raw.index('='))
		name_part = raw[:split_index]
		params_part = raw[split_index+1:].split(':')

	block = _coerce_block_type(name_part, strict=strict)
	if block is None:
		return None
	if len(block.properties) == 0:
		return _Blocks({block:set(tuple())})
	
	def _parse_param(param:str) -> _StateFilter:
		param_name, param_value = param.split('=')
		return lambda block:getattr(block, param_name) == param_value
	return _Blocks([block], filter=_filters.all(*[_parse_param(param) for param in params_part]))