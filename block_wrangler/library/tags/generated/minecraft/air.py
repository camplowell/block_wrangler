from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:air')
	
	tag.add(block_types(
		'minecraft:void_air',
		'minecraft:air',
		'minecraft:cave_air',
	strict=False))