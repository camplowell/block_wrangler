from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:stone_bricks')
	
	tag.add(block_types(
		'minecraft:chiseled_stone_bricks',
		'minecraft:stone_bricks',
		'minecraft:mossy_stone_bricks',
		'minecraft:cracked_stone_bricks',
	strict=False))