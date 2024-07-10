from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:small_flowers')
	
	tag.add(block_types(
		'minecraft:oxeye_daisy',
		'minecraft:pink_tulip',
		'minecraft:dandelion',
		'minecraft:poppy',
		'minecraft:azure_bluet',
		'minecraft:white_tulip',
		'minecraft:blue_orchid',
		'minecraft:orange_tulip',
		'minecraft:lily_of_the_valley',
		'minecraft:torchflower',
		'minecraft:red_tulip',
		'minecraft:allium',
		'minecraft:wither_rose',
		'minecraft:cornflower',
	strict=False))