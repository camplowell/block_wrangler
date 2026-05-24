from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_shelves')
	
	tag.add(block_types(
		'minecraft:acacia_shelf',
		'minecraft:bamboo_shelf',
		'minecraft:birch_shelf',
		'minecraft:cherry_shelf',
		'minecraft:crimson_shelf',
		'minecraft:dark_oak_shelf',
		'minecraft:jungle_shelf',
		'minecraft:mangrove_shelf',
		'minecraft:oak_shelf',
		'minecraft:pale_oak_shelf',
		'minecraft:spruce_shelf',
		'minecraft:warped_shelf',
	strict=False))