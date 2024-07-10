from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_buttons')
	
	tag.add(block_types(
		'minecraft:spruce_button',
		'minecraft:dark_oak_button',
		'minecraft:cherry_button',
		'minecraft:bamboo_button',
		'minecraft:birch_button',
		'minecraft:warped_button',
		'minecraft:jungle_button',
		'minecraft:crimson_button',
		'minecraft:acacia_button',
		'minecraft:oak_button',
		'minecraft:mangrove_button',
	strict=False))