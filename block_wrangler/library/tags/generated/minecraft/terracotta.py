from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:terracotta')
	
	tag.add(block_types(
		'minecraft:yellow_terracotta',
		'minecraft:red_terracotta',
		'minecraft:light_gray_terracotta',
		'minecraft:purple_terracotta',
		'minecraft:blue_terracotta',
		'minecraft:brown_terracotta',
		'minecraft:orange_terracotta',
		'minecraft:green_terracotta',
		'minecraft:gray_terracotta',
		'minecraft:terracotta',
		'minecraft:pink_terracotta',
		'minecraft:lime_terracotta',
		'minecraft:cyan_terracotta',
		'minecraft:black_terracotta',
		'minecraft:magenta_terracotta',
		'minecraft:white_terracotta',
		'minecraft:light_blue_terracotta',
	strict=False))