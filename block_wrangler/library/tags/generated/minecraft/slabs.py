from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:slabs')
	tag.add(library.touch('minecraft:wooden_slabs'))
	
	tag.add(block_types(
		'minecraft:polished_diorite_slab',
		'minecraft:polished_blackstone_brick_slab',
		'minecraft:petrified_oak_slab',
		'minecraft:red_nether_brick_slab',
		'minecraft:polished_andesite_slab',
		'minecraft:exposed_cut_copper_slab',
		'minecraft:waxed_exposed_cut_copper_slab',
		'minecraft:polished_deepslate_slab',
		'minecraft:cobbled_deepslate_slab',
		'minecraft:weathered_cut_copper_slab',
		'minecraft:tuff_slab',
		'minecraft:blackstone_slab',
		'minecraft:deepslate_tile_slab',
		'minecraft:cobblestone_slab',
		'minecraft:red_sandstone_slab',
		'minecraft:stone_brick_slab',
		'minecraft:stone_slab',
		'minecraft:bamboo_mosaic_slab',
		'minecraft:deepslate_brick_slab',
		'minecraft:tuff_brick_slab',
		'minecraft:cut_sandstone_slab',
		'minecraft:waxed_cut_copper_slab',
		'minecraft:nether_brick_slab',
		'minecraft:mossy_cobblestone_slab',
		'minecraft:smooth_red_sandstone_slab',
		'minecraft:waxed_oxidized_cut_copper_slab',
		'minecraft:prismarine_brick_slab',
		'minecraft:waxed_weathered_cut_copper_slab',
		'minecraft:polished_granite_slab',
		'minecraft:dark_prismarine_slab',
		'minecraft:purpur_slab',
		'minecraft:smooth_sandstone_slab',
		'minecraft:prismarine_slab',
		'minecraft:sandstone_slab',
		'minecraft:end_stone_brick_slab',
		'minecraft:polished_blackstone_slab',
		'minecraft:quartz_slab',
		'minecraft:smooth_quartz_slab',
		'minecraft:diorite_slab',
		'minecraft:mud_brick_slab',
		'minecraft:brick_slab',
		'minecraft:oxidized_cut_copper_slab',
		'minecraft:polished_tuff_slab',
		'minecraft:andesite_slab',
		'minecraft:smooth_stone_slab',
		'minecraft:granite_slab',
		'minecraft:cut_copper_slab',
		'minecraft:mossy_stone_brick_slab',
		'minecraft:cut_red_sandstone_slab',
	strict=False))