from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:small_flowers')
	
	tag.add(block_types(
		'minecraft:allium',
		'minecraft:azure_bluet',
		'minecraft:blue_orchid',
		'minecraft:closed_eyeblossom',
		'minecraft:cornflower',
		'minecraft:dandelion',
		'minecraft:lily_of_the_valley',
		'minecraft:open_eyeblossom',
		'minecraft:orange_tulip',
		'minecraft:oxeye_daisy',
		'minecraft:pink_tulip',
		'minecraft:poppy',
		'minecraft:red_tulip',
		'minecraft:torchflower',
		'minecraft:white_tulip',
		'minecraft:wither_rose',
	strict=False))