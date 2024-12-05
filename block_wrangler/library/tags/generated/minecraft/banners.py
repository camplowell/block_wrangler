from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:banners')
	
	tag.add(block_types(
		'minecraft:black_banner',
		'minecraft:black_wall_banner',
		'minecraft:blue_banner',
		'minecraft:blue_wall_banner',
		'minecraft:brown_banner',
		'minecraft:brown_wall_banner',
		'minecraft:cyan_banner',
		'minecraft:cyan_wall_banner',
		'minecraft:gray_banner',
		'minecraft:gray_wall_banner',
		'minecraft:green_banner',
		'minecraft:green_wall_banner',
		'minecraft:light_blue_banner',
		'minecraft:light_blue_wall_banner',
		'minecraft:light_gray_banner',
		'minecraft:light_gray_wall_banner',
		'minecraft:lime_banner',
		'minecraft:lime_wall_banner',
		'minecraft:magenta_banner',
		'minecraft:magenta_wall_banner',
		'minecraft:orange_banner',
		'minecraft:orange_wall_banner',
		'minecraft:pink_banner',
		'minecraft:pink_wall_banner',
		'minecraft:purple_banner',
		'minecraft:purple_wall_banner',
		'minecraft:red_banner',
		'minecraft:red_wall_banner',
		'minecraft:white_banner',
		'minecraft:white_wall_banner',
		'minecraft:yellow_banner',
		'minecraft:yellow_wall_banner',
	strict=False))