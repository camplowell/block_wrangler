from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:frogs_spawnable_on')
	
	tag.add(block_types(
		'minecraft:grass_block',
		'minecraft:mangrove_roots',
		'minecraft:mud',
		'minecraft:muddy_mangrove_roots',
	strict=False))