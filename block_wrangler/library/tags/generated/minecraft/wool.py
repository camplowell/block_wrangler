from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wool')
	
	tag.add(block_types(
		'minecraft:black_wool',
		'minecraft:blue_wool',
		'minecraft:brown_wool',
		'minecraft:cyan_wool',
		'minecraft:gray_wool',
		'minecraft:green_wool',
		'minecraft:light_blue_wool',
		'minecraft:light_gray_wool',
		'minecraft:lime_wool',
		'minecraft:magenta_wool',
		'minecraft:orange_wool',
		'minecraft:pink_wool',
		'minecraft:purple_wool',
		'minecraft:red_wool',
		'minecraft:white_wool',
		'minecraft:yellow_wool',
	strict=False))