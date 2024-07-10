from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:ancient_city_replaceable')
	
	tag.add(block_types(
		'minecraft:deepslate_tiles',
		'minecraft:deepslate_brick_stairs',
		'minecraft:deepslate_tile_slab',
		'minecraft:deepslate',
		'minecraft:deepslate_brick_wall',
		'minecraft:deepslate_bricks',
		'minecraft:deepslate_brick_slab',
		'minecraft:gray_wool',
		'minecraft:cobbled_deepslate',
		'minecraft:cracked_deepslate_bricks',
		'minecraft:cracked_deepslate_tiles',
		'minecraft:deepslate_tile_wall',
	strict=False))