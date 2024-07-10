
from enum import Enum
from pathlib import Path
from typing import Dict, Iterable
from jinja2 import Environment, FileSystemLoader

from block_wrangler import BlockType
from block_wrangler.library import blocks as block_library, factories

env = Environment(loader=FileSystemLoader(Path(__file__).resolve().parent / 'templates'))

def add_blocks(blocks:Iterable[BlockType], blocks_folder:Path):
	updated_library:Dict[str, Dict[str, BlockType]] = {}
	skipped = 0
	overwritten = 0
	added = 0
	for block in blocks:
		if block.namespace not in updated_library:
			updated_library[block.namespace] = factories._block_namespace(block.namespace, strict=False).copy()
		if block.name in updated_library[block.namespace]:
			if updated_library[block.namespace][block.name] == block:
				skipped += 1
				continue
			else:
				overwritten += 1
		else:
			added += 1
		updated_library[block.namespace][block.name] = block
	template = env.get_template('block_namespace.py.jinja')
	print(f'Added {added} blocks, Skipped {skipped} blocks, overwrote {overwritten} blocks')
	for namespace, namespace_blocks in updated_library.items():
		if namespace_blocks == factories._block_namespace(namespace, strict=False):
			print(f'Skipping {namespace} ({len(namespace_blocks)} blocks)')
			continue
		namespace_file = blocks_folder / f'{namespace}.py'
		namespace_code = template.render(blocks=namespace_blocks.values())
		with namespace_file.open('w') as f:
			f.write(namespace_code)
		print(f'Updated {namespace} ({len(namespace_blocks)} blocks)')

class BlockParser(Enum):
	MC_DATA = 'mc-data'
	VANILLA = 'vanilla'
	
	def parse(self, raw_blocks):
		match self:
			case BlockParser.MC_DATA:
				return parse_mc_data_blocks(raw_blocks)
			case BlockParser.VANILLA:
				return parse_vanilla_blocks(raw_blocks)


def parse_vanilla_blocks(raw_blocks:dict):
	for block_name, block_shape in raw_blocks.items():
		namespace, name = block_name.split(':') if ':' in block_name else ('minecraft', block_name)
		props = {name:tuple(values) for name, values in block_shape.get('properties', {}).items()}
		yield BlockType(namespace, name, props)

def parse_mc_data_blocks(raw_blocks:list):
	for raw_block in raw_blocks:
		namespace, name = raw_block['name'].split(':') if ':' in raw_block['name'] else ('minecraft', raw_block['name'])
		props = {prop['name']:tuple(prop.get('values', ('false', 'true'))) for prop in raw_block['states']}
		yield BlockType(namespace, name, props)
