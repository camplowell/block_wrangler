from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:beacon_base_blocks')
	
	tag.add(block_types(
		'minecraft:diamond_block',
		'minecraft:emerald_block',
		'minecraft:gold_block',
		'minecraft:iron_block',
		'minecraft:netherite_block',
	strict=False))