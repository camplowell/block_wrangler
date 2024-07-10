from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:beds')
	
	tag.add(block_types(
		'minecraft:lime_bed',
		'minecraft:purple_bed',
		'minecraft:green_bed',
		'minecraft:light_gray_bed',
		'minecraft:gray_bed',
		'minecraft:orange_bed',
		'minecraft:magenta_bed',
		'minecraft:blue_bed',
		'minecraft:white_bed',
		'minecraft:pink_bed',
		'minecraft:red_bed',
		'minecraft:light_blue_bed',
		'minecraft:yellow_bed',
		'minecraft:black_bed',
		'minecraft:brown_bed',
		'minecraft:cyan_bed',
	strict=False))