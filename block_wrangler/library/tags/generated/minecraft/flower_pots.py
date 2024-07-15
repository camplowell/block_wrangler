from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:flower_pots')
	
	tag.add(block_types(
		'minecraft:potted_lily_of_the_valley',
		'minecraft:potted_flowering_azalea_bush',
		'minecraft:potted_jungle_sapling',
		'minecraft:potted_acacia_sapling',
		'minecraft:potted_birch_sapling',
		'minecraft:potted_spruce_sapling',
		'minecraft:potted_red_mushroom',
		'minecraft:potted_dandelion',
		'minecraft:potted_oak_sapling',
		'minecraft:potted_pink_tulip',
		'minecraft:potted_dead_bush',
		'minecraft:potted_cornflower',
		'minecraft:potted_orange_tulip',
		'minecraft:potted_oxeye_daisy',
		'minecraft:potted_azalea_bush',
		'minecraft:potted_poppy',
		'minecraft:potted_crimson_roots',
		'minecraft:potted_mangrove_propagule',
		'minecraft:potted_wither_rose',
		'minecraft:potted_brown_mushroom',
		'minecraft:potted_azure_bluet',
		'minecraft:potted_dark_oak_sapling',
		'minecraft:potted_white_tulip',
		'minecraft:potted_allium',
		'minecraft:potted_warped_fungus',
		'minecraft:potted_fern',
		'minecraft:potted_bamboo',
		'minecraft:potted_torchflower',
		'minecraft:potted_crimson_fungus',
		'minecraft:flower_pot',
		'minecraft:potted_warped_roots',
		'minecraft:potted_blue_orchid',
		'minecraft:potted_red_tulip',
		'minecraft:potted_cactus',
		'minecraft:potted_cherry_sapling',
	strict=False))