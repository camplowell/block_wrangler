from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:planks')
	
	tag.add(block_types(
		'minecraft:crimson_planks',
		'minecraft:jungle_planks',
		'minecraft:warped_planks',
		'minecraft:birch_planks',
		'minecraft:oak_planks',
		'minecraft:mangrove_planks',
		'minecraft:bamboo_planks',
		'minecraft:acacia_planks',
		'minecraft:cherry_planks',
		'minecraft:spruce_planks',
		'minecraft:dark_oak_planks',
	strict=False))