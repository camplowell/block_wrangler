from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wall_hanging_signs')
	
	tag.add(block_types(
		'minecraft:spruce_wall_hanging_sign',
		'minecraft:acacia_wall_hanging_sign',
		'minecraft:dark_oak_wall_hanging_sign',
		'minecraft:jungle_wall_hanging_sign',
		'minecraft:bamboo_wall_hanging_sign',
		'minecraft:cherry_wall_hanging_sign',
		'minecraft:mangrove_wall_hanging_sign',
		'minecraft:crimson_wall_hanging_sign',
		'minecraft:oak_wall_hanging_sign',
		'minecraft:warped_wall_hanging_sign',
		'minecraft:birch_wall_hanging_sign',
	strict=False))