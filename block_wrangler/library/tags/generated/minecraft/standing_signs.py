from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:standing_signs')
	
	tag.add(block_types(
		'minecraft:acacia_sign',
		'minecraft:bamboo_sign',
		'minecraft:birch_sign',
		'minecraft:cherry_sign',
		'minecraft:crimson_sign',
		'minecraft:dark_oak_sign',
		'minecraft:jungle_sign',
		'minecraft:mangrove_sign',
		'minecraft:oak_sign',
		'minecraft:pale_oak_sign',
		'minecraft:spruce_sign',
		'minecraft:warped_sign',
	strict=False))