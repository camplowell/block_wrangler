from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:mineable/hoe')
	
	tag.add(block_types(
		'minecraft:acacia_leaves',
		'minecraft:azalea_leaves',
		'minecraft:birch_leaves',
		'minecraft:calibrated_sculk_sensor',
		'minecraft:cherry_leaves',
		'minecraft:dark_oak_leaves',
		'minecraft:dried_kelp_block',
		'minecraft:flowering_azalea_leaves',
		'minecraft:hay_block',
		'minecraft:jungle_leaves',
		'minecraft:mangrove_leaves',
		'minecraft:moss_block',
		'minecraft:moss_carpet',
		'minecraft:nether_wart_block',
		'minecraft:oak_leaves',
		'minecraft:pale_moss_block',
		'minecraft:pale_moss_carpet',
		'minecraft:pale_oak_leaves',
		'minecraft:pink_petals',
		'minecraft:sculk',
		'minecraft:sculk_catalyst',
		'minecraft:sculk_sensor',
		'minecraft:sculk_shrieker',
		'minecraft:sculk_vein',
		'minecraft:shroomlight',
		'minecraft:sponge',
		'minecraft:spruce_leaves',
		'minecraft:target',
		'minecraft:warped_wart_block',
		'minecraft:wet_sponge',
	strict=False))