import json
from pathlib import Path
import re
from typing import Any, Callable, Dict, List, NotRequired, Tuple, TypedDict
from block_wrangler.library.factories import load_tags, gather_block_types

docs_lib = Path('./static/library')

def main():
	write(bake_tags(), docs_lib.joinpath('tags.json'))
	write(bake_blocks(), docs_lib.joinpath('blocks.json'))
	
Metadata = Dict[str, Any]
TreeNode = TypedDict('TreeNode', {
	'name': str,
	'children': NotRequired[List['TreeNode']],
	'metadata': NotRequired[Metadata]
})

def write(tags:TreeNode, path:Path):
	with path.open('w') as f:
		json.dump(tags, f, separators=(',', ':'), indent=2)

def bake_tags():
	def tag_parent_info(name:str, prev_metadata:Metadata|None) -> Tuple[str, Metadata|None]|None:
		if '/' in name:
			return name[:name.index('/')], None
		elif ':' in name:
			return name[:name.index(':')], {'namespace': True}
		elif prev_metadata is None:
			return 'Block Wrangler', {'namespace': True}
	library:TreeNode = {'name':'', 'children':[]}
	for tag in load_tags().tags.keys():
		touch_node(library, tag, None, tag_parent_info)
	intuitive_sort(library)

	return library

def intuitive_sort(node:TreeNode):
	if 'children' not in node:
		return
	number_blocker = re.compile(r'\D|\d+')
	def intuitive_key(node:TreeNode) -> Tuple[Tuple[int, int|str], ...]:
		tokens = re.findall(number_blocker, node['name'])
		ret = []
		for token in tokens:
			if token.isdigit():
				ret.append((1, int(token)))
			else:
				ret.append((0, token))
		return tuple(ret)
	node['children'].sort(key=intuitive_key)
	for child in node['children']:
		intuitive_sort(child)

def bake_blocks():
	library:TreeNode = {'name':'', 'children':[]}
	def block_parent_info(name:str, prev_metadata:Metadata|None) -> Tuple[str, Metadata|None]|None:
		if prev_metadata is not None:
			return name[:name.index(':')] if ':' in name else 'minecraft', None
		return None
	for block in gather_block_types():
		touch_node(library, block.name, block.properties, block_parent_info)
	intuitive_sort(library)
	return library

def touch_node[T:Metadata](root:TreeNode, name:str, metadata:T|None, get_parent_info:Callable[[str, T|None], Tuple[str, T|None]|None]) -> TreeNode:
	parent_info:Tuple[str, T|None]|None = get_parent_info(name, metadata)
	parent = root
	if parent_info:
		parent = touch_node(root, *parent_info, get_parent_info)
	result:TreeNode|None = None
	if 'children' in parent:
		result = next((child for child in parent['children'] if child['name'] == name), None)
	else:
		parent['children'] = []
	if result is None:
		result = {
			'name': name,
			'metadata': metadata
		} if metadata else {
			'name': name
		}
		parent['children'].append(result)
	return result

JsonTag = Dict[str, 'JsonTag']
JsonTagNamespace = TypedDict('JsonTagNamespace', {
	'ignore': bool,
	'tags': JsonTag,
})

if __name__ == "__main__":
	main()