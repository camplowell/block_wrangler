from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:ceiling_hanging_signs')
	
	tag.add(block_types(
		'minecraft:crimson_hanging_sign',
		'minecraft:bamboo_hanging_sign',
		'minecraft:warped_hanging_sign',
		'minecraft:oak_hanging_sign',
		'minecraft:jungle_hanging_sign',
		'minecraft:spruce_hanging_sign',
		'minecraft:cherry_hanging_sign',
		'minecraft:dark_oak_hanging_sign',
		'minecraft:birch_hanging_sign',
		'minecraft:mangrove_hanging_sign',
		'minecraft:acacia_hanging_sign',
	strict=False))