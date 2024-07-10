from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:mineable/hoe')
	
	tag.add(block_types(
		'minecraft:mangrove_leaves',
		'minecraft:warped_wart_block',
		'minecraft:jungle_leaves',
		'minecraft:sculk_sensor',
		'minecraft:dried_kelp_block',
		'minecraft:target',
		'minecraft:sponge',
		'minecraft:acacia_leaves',
		'minecraft:azalea_leaves',
		'minecraft:wet_sponge',
		'minecraft:flowering_azalea_leaves',
		'minecraft:sculk_shrieker',
		'minecraft:cherry_leaves',
		'minecraft:calibrated_sculk_sensor',
		'minecraft:birch_leaves',
		'minecraft:pink_petals',
		'minecraft:dark_oak_leaves',
		'minecraft:nether_wart_block',
		'minecraft:oak_leaves',
		'minecraft:sculk_vein',
		'minecraft:spruce_leaves',
		'minecraft:sculk',
		'minecraft:shroomlight',
		'minecraft:moss_carpet',
		'minecraft:moss_block',
		'minecraft:hay_block',
		'minecraft:sculk_catalyst',
	strict=False))