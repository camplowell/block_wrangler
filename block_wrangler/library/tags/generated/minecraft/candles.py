from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:candles')
	
	tag.add(block_types(
		'minecraft:brown_candle',
		'minecraft:pink_candle',
		'minecraft:cyan_candle',
		'minecraft:blue_candle',
		'minecraft:green_candle',
		'minecraft:red_candle',
		'minecraft:magenta_candle',
		'minecraft:white_candle',
		'minecraft:purple_candle',
		'minecraft:orange_candle',
		'minecraft:black_candle',
		'minecraft:light_blue_candle',
		'minecraft:yellow_candle',
		'minecraft:candle',
		'minecraft:light_gray_candle',
		'minecraft:gray_candle',
		'minecraft:lime_candle',
	strict=False))