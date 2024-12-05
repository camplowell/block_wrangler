from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_buttons')
	
	tag.add(block_types(
		'minecraft:acacia_button',
		'minecraft:bamboo_button',
		'minecraft:birch_button',
		'minecraft:cherry_button',
		'minecraft:crimson_button',
		'minecraft:dark_oak_button',
		'minecraft:jungle_button',
		'minecraft:mangrove_button',
		'minecraft:oak_button',
		'minecraft:pale_oak_button',
		'minecraft:spruce_button',
		'minecraft:warped_button',
	strict=False))