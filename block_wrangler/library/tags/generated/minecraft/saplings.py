from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:saplings')
	
	tag.add(block_types(
		'minecraft:mangrove_propagule',
		'minecraft:azalea',
		'minecraft:spruce_sapling',
		'minecraft:birch_sapling',
		'minecraft:acacia_sapling',
		'minecraft:cherry_sapling',
		'minecraft:dark_oak_sapling',
		'minecraft:oak_sapling',
		'minecraft:jungle_sapling',
		'minecraft:flowering_azalea',
	strict=False))