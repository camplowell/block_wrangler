import argparse, json
import os
from pathlib import Path
from typing import Dict, List

from block_importer import BlockParser, add_blocks
from tag_importer import add_tags, TagType

block_wrangler_path = Path(__file__).parent.parent.joinpath('block_wrangler')
#testing_path = Path(__file__).parent.parent.joinpath('importer_tests/')

def import_blocks(file:str, parser:BlockParser = BlockParser.MC_DATA):
	with Path(file).resolve().open('r') as f:
		raw_blocks:List[dict] = json.load(f)

	block_folder = block_wrangler_path.joinpath('library/blocks')
	add_blocks(parser.parse(raw_blocks), block_folder)

def import_tags(folder:str, namespace:str, *path:str):
	tags:Dict[str, TagType] = {}
	folder_path = Path(folder).resolve()
	for file in (folder_path.joinpath(f) for f in os.listdir(folder_path)):
		if file.is_dir():
			import_tags(str(file), namespace, file.name)
			continue
		elif file.suffix.lower() != '.json':
			continue
		
		with file.open('r') as f:
			values = json.load(f)["values"]
		tag_name = f"{namespace}:{'/'.join((*path, file.stem))}"
		tags[tag_name] = {
			'name':tag_name,
			'blocks': set([value for value in values if not value.startswith('#')]),
			'dependencies':set([value[1:] for value in values if value.startswith('#')])
		}
	
	base_path = block_wrangler_path.joinpath('library/tags/generated').resolve()
	add_tags(tags, base_path)

def import_mc_data(folder:str):
	mcdata_root = Path(folder).resolve()
	if (reports := mcdata_root.joinpath('reports')).exists():
		import_blocks(str(reports.joinpath('blocks.json')), BlockParser.VANILLA)
	if (data := mcdata_root.joinpath('data')).exists():
		for namespace in data.iterdir():
			if namespace.stem.startswith('.'):
				continue
			import_tags(str(namespace.joinpath('tags/block')), namespace.stem)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
blocks_cmd = subparsers.add_parser('blocks', help='Import blocks from a minecraft_data style JSON file')
blocks_cmd.add_argument('file', type=str, help='The JSON file to import blocks from')
blocks_cmd.add_argument('--parser', type=BlockParser, default=BlockParser.MC_DATA, help='The parser to use (either vanilla or mc-data)')
blocks_cmd.set_defaults(func=import_blocks)

tags_cmd = subparsers.add_parser('tags', help='Import tags')
tags_cmd.add_argument('folder', type=str, help='The folder to import tags from')
tags_cmd.add_argument('namespace', type=str, help='The namespace to use for the tags')
tags_cmd.set_defaults(func=import_tags)

mc_cmd = subparsers.add_parser('data-generator', help='Import everything from the minecraft data generator')
mc_cmd.add_argument('folder', type=str, help='The folder to import from')
mc_cmd.set_defaults(func=import_mc_data)

if __name__ == '__main__':
	args = parser.parse_args()
	func = args.func
	delattr(args, 'func')
	func(**vars(args))