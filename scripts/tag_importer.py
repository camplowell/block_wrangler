

import importlib
from itertools import accumulate
from pathlib import Path
import re
from typing import Dict, List, Set, TypedDict
from jinja2 import Environment, FileSystemLoader

from block_wrangler import Tag, TagLibrary
from block_wrangler.library.tags import generated as generated_tags

TagType = TypedDict('TagType', {'name':str, 'blocks':Set[str], 'dependencies':Set[str]})
env = Environment(loader=FileSystemLoader(Path(__file__).resolve().parent / 'templates'))

def merge(a:Set[str], b:List[str]):
	return list(set(a) | set(b))

def add_tags(tags:Dict[str, TagType], tags_folder:Path):
	template = env.get_template('tag.py.jinja')
	for tag_name, tag_values in tags.items():
		if tag_name == 'minecraft:air':
			continue
		tag_path = re.split(r'[\/:]', tag_name)
		for folder in accumulate(tag_path[:-1], lambda a, b: a.joinpath(b), initial=tags_folder):
			if not folder.exists():
				folder.mkdir(parents=True, exist_ok=True)
			folder.joinpath('__init__.py').touch()

		tag_file = tags_folder.joinpath(*tag_path[:-1], tag_path[-1] + '.py')
		try:
			tag_module = importlib.import_module('.' + '.'.join(tag_path), package=generated_tags.__name__)
			tag_library = TagLibrary()
			tag_module.load_tags(tag_library)
			existing_blocks = tag_library.touch(tag_name)._filters.keys()
			existing_sources = tag_library.touch(tag_name).sources.keys() # generated tags don't filter their sources
			num_blocks = len(existing_blocks)
			num_sources = len(existing_sources)
			tag_values['blocks'] = set([str(block) for block in existing_blocks]) | tag_values['blocks']
			tag_values['dependencies'] |= set([str(block) for block in existing_sources])
			if num_blocks != len(tag_values['blocks']) or num_sources != len(tag_values['dependencies']):
				print(f"Modifying tag {tag_name} (added {len(tag_values['blocks']) - num_blocks} blocks, {len(tag_values['dependencies']) - num_sources} sources)")
		except ModuleNotFoundError as e:
			print(f'Creating new tag {tag_name} ({e})')
		rendered = template.render(**{
			'name': tag_values['name'],
			'blocks': sorted(tag_values['blocks']),
			'dependencies': sorted(tag_values['dependencies'])
		})

		with tag_file.open('w') as f:
			f.write(rendered)