from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wool_carpets')
	
	tag.add(block_types(
		'minecraft:light_blue_carpet',
		'minecraft:purple_carpet',
		'minecraft:yellow_carpet',
		'minecraft:blue_carpet',
		'minecraft:red_carpet',
		'minecraft:lime_carpet',
		'minecraft:black_carpet',
		'minecraft:pink_carpet',
		'minecraft:white_carpet',
		'minecraft:orange_carpet',
		'minecraft:magenta_carpet',
		'minecraft:gray_carpet',
		'minecraft:brown_carpet',
		'minecraft:cyan_carpet',
		'minecraft:green_carpet',
		'minecraft:light_gray_carpet',
	strict=False))