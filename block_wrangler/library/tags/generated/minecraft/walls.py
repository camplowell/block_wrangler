from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:walls')
	
	tag.add(block_types(
		'minecraft:polished_blackstone_brick_wall',
		'minecraft:diorite_wall',
		'minecraft:andesite_wall',
		'minecraft:cobblestone_wall',
		'minecraft:red_nether_brick_wall',
		'minecraft:granite_wall',
		'minecraft:brick_wall',
		'minecraft:polished_tuff_wall',
		'minecraft:red_sandstone_wall',
		'minecraft:end_stone_brick_wall',
		'minecraft:polished_deepslate_wall',
		'minecraft:mossy_cobblestone_wall',
		'minecraft:cobbled_deepslate_wall',
		'minecraft:nether_brick_wall',
		'minecraft:mossy_stone_brick_wall',
		'minecraft:prismarine_wall',
		'minecraft:tuff_brick_wall',
		'minecraft:polished_blackstone_wall',
		'minecraft:sandstone_wall',
		'minecraft:deepslate_brick_wall',
		'minecraft:mud_brick_wall',
		'minecraft:blackstone_wall',
		'minecraft:tuff_wall',
		'minecraft:stone_brick_wall',
		'minecraft:deepslate_tile_wall',
	strict=False))