from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:grass_blocks')
	
	tag.add(block_types(
		'minecraft:grass_block',
		'minecraft:mycelium',
		'minecraft:podzol',
	strict=False))