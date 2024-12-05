from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:ice')
	
	tag.add(block_types(
		'minecraft:blue_ice',
		'minecraft:frosted_ice',
		'minecraft:ice',
		'minecraft:packed_ice',
	strict=False))