from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:candles')
	
	tag.add(block_types(
		'minecraft:black_candle',
		'minecraft:blue_candle',
		'minecraft:brown_candle',
		'minecraft:candle',
		'minecraft:cyan_candle',
		'minecraft:gray_candle',
		'minecraft:green_candle',
		'minecraft:light_blue_candle',
		'minecraft:light_gray_candle',
		'minecraft:lime_candle',
		'minecraft:magenta_candle',
		'minecraft:orange_candle',
		'minecraft:pink_candle',
		'minecraft:purple_candle',
		'minecraft:red_candle',
		'minecraft:white_candle',
		'minecraft:yellow_candle',
	strict=False))