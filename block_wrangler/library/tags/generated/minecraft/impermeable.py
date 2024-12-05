from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:impermeable')
	
	tag.add(block_types(
		'minecraft:black_stained_glass',
		'minecraft:blue_stained_glass',
		'minecraft:brown_stained_glass',
		'minecraft:cyan_stained_glass',
		'minecraft:glass',
		'minecraft:gray_stained_glass',
		'minecraft:green_stained_glass',
		'minecraft:light_blue_stained_glass',
		'minecraft:light_gray_stained_glass',
		'minecraft:lime_stained_glass',
		'minecraft:magenta_stained_glass',
		'minecraft:orange_stained_glass',
		'minecraft:pink_stained_glass',
		'minecraft:purple_stained_glass',
		'minecraft:red_stained_glass',
		'minecraft:tinted_glass',
		'minecraft:white_stained_glass',
		'minecraft:yellow_stained_glass',
	strict=False))