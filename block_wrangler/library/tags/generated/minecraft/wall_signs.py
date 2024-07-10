from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wall_signs')
	
	tag.add(block_types(
		'minecraft:warped_wall_sign',
		'minecraft:cherry_wall_sign',
		'minecraft:bamboo_wall_sign',
		'minecraft:acacia_wall_sign',
		'minecraft:spruce_wall_sign',
		'minecraft:birch_wall_sign',
		'minecraft:dark_oak_wall_sign',
		'minecraft:crimson_wall_sign',
		'minecraft:jungle_wall_sign',
		'minecraft:mangrove_wall_sign',
		'minecraft:oak_wall_sign',
	strict=False))