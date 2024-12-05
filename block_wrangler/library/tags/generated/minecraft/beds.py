from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:beds')
	
	tag.add(block_types(
		'minecraft:black_bed',
		'minecraft:blue_bed',
		'minecraft:brown_bed',
		'minecraft:cyan_bed',
		'minecraft:gray_bed',
		'minecraft:green_bed',
		'minecraft:light_blue_bed',
		'minecraft:light_gray_bed',
		'minecraft:lime_bed',
		'minecraft:magenta_bed',
		'minecraft:orange_bed',
		'minecraft:pink_bed',
		'minecraft:purple_bed',
		'minecraft:red_bed',
		'minecraft:white_bed',
		'minecraft:yellow_bed',
	strict=False))