from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:candle_cakes')
	
	tag.add(block_types(
		'minecraft:lime_candle_cake',
		'minecraft:orange_candle_cake',
		'minecraft:pink_candle_cake',
		'minecraft:light_gray_candle_cake',
		'minecraft:yellow_candle_cake',
		'minecraft:cyan_candle_cake',
		'minecraft:candle_cake',
		'minecraft:white_candle_cake',
		'minecraft:purple_candle_cake',
		'minecraft:red_candle_cake',
		'minecraft:light_blue_candle_cake',
		'minecraft:black_candle_cake',
		'minecraft:gray_candle_cake',
		'minecraft:green_candle_cake',
		'minecraft:magenta_candle_cake',
		'minecraft:brown_candle_cake',
		'minecraft:blue_candle_cake',
	strict=False))