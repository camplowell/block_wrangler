from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:soul_fire_base_blocks')
	
	tag.add(block_types(
		'minecraft:soul_soil',
		'minecraft:soul_sand',
	strict=False))