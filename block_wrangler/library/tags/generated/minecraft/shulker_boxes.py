from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:shulker_boxes')
	
	tag.add(block_types(
		'minecraft:black_shulker_box',
		'minecraft:blue_shulker_box',
		'minecraft:brown_shulker_box',
		'minecraft:cyan_shulker_box',
		'minecraft:gray_shulker_box',
		'minecraft:green_shulker_box',
		'minecraft:light_blue_shulker_box',
		'minecraft:light_gray_shulker_box',
		'minecraft:lime_shulker_box',
		'minecraft:magenta_shulker_box',
		'minecraft:orange_shulker_box',
		'minecraft:pink_shulker_box',
		'minecraft:purple_shulker_box',
		'minecraft:red_shulker_box',
		'minecraft:shulker_box',
		'minecraft:white_shulker_box',
		'minecraft:yellow_shulker_box',
	strict=False))