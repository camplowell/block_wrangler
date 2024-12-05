from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:saplings')
	
	tag.add(block_types(
		'minecraft:acacia_sapling',
		'minecraft:azalea',
		'minecraft:birch_sapling',
		'minecraft:cherry_sapling',
		'minecraft:dark_oak_sapling',
		'minecraft:flowering_azalea',
		'minecraft:jungle_sapling',
		'minecraft:mangrove_propagule',
		'minecraft:oak_sapling',
		'minecraft:pale_oak_sapling',
		'minecraft:spruce_sapling',
	strict=False))