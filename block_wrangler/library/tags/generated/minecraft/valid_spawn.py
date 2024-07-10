from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:valid_spawn')
	
	tag.add(block_types(
		'minecraft:grass_block',
		'minecraft:podzol',
	strict=False))