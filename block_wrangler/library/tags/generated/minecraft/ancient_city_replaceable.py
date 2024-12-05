from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:ancient_city_replaceable')
	
	tag.add(block_types(
		'minecraft:cobbled_deepslate',
		'minecraft:cracked_deepslate_bricks',
		'minecraft:cracked_deepslate_tiles',
		'minecraft:deepslate',
		'minecraft:deepslate_brick_slab',
		'minecraft:deepslate_brick_stairs',
		'minecraft:deepslate_brick_wall',
		'minecraft:deepslate_bricks',
		'minecraft:deepslate_tile_slab',
		'minecraft:deepslate_tile_wall',
		'minecraft:deepslate_tiles',
		'minecraft:gray_wool',
	strict=False))