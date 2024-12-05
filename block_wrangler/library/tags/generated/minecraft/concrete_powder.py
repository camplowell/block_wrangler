from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:concrete_powder')
	
	tag.add(block_types(
		'minecraft:black_concrete_powder',
		'minecraft:blue_concrete_powder',
		'minecraft:brown_concrete_powder',
		'minecraft:cyan_concrete_powder',
		'minecraft:gray_concrete_powder',
		'minecraft:green_concrete_powder',
		'minecraft:light_blue_concrete_powder',
		'minecraft:light_gray_concrete_powder',
		'minecraft:lime_concrete_powder',
		'minecraft:magenta_concrete_powder',
		'minecraft:orange_concrete_powder',
		'minecraft:pink_concrete_powder',
		'minecraft:purple_concrete_powder',
		'minecraft:red_concrete_powder',
		'minecraft:white_concrete_powder',
		'minecraft:yellow_concrete_powder',
	strict=False))