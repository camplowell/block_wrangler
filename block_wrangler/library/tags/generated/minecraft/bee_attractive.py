from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:bee_attractive')
	
	tag.add(block_types(
		'minecraft:allium',
		'minecraft:azure_bluet',
		'minecraft:blue_orchid',
		'minecraft:cactus_flower',
		'minecraft:cherry_leaves',
		'minecraft:chorus_flower',
		'minecraft:cornflower',
		'minecraft:dandelion',
		'minecraft:flowering_azalea',
		'minecraft:flowering_azalea_leaves',
		'minecraft:lilac',
		'minecraft:lily_of_the_valley',
		'minecraft:mangrove_propagule',
		'minecraft:open_eyeblossom',
		'minecraft:orange_tulip',
		'minecraft:oxeye_daisy',
		'minecraft:peony',
		'minecraft:pink_petals',
		'minecraft:pink_tulip',
		'minecraft:pitcher_plant',
		'minecraft:poppy',
		'minecraft:red_tulip',
		'minecraft:rose_bush',
		'minecraft:spore_blossom',
		'minecraft:sunflower',
		'minecraft:torchflower',
		'minecraft:white_tulip',
		'minecraft:wildflowers',
		'minecraft:wither_rose',
	strict=False))