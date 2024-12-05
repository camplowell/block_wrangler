from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:soul_speed_blocks')
	
	tag.add(block_types(
		'minecraft:soul_sand',
		'minecraft:soul_soil',
	strict=False))