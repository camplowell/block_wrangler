from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_stairs')
	
	tag.add(block_types(
		'minecraft:acacia_stairs',
		'minecraft:bamboo_stairs',
		'minecraft:birch_stairs',
		'minecraft:cherry_stairs',
		'minecraft:crimson_stairs',
		'minecraft:dark_oak_stairs',
		'minecraft:jungle_stairs',
		'minecraft:mangrove_stairs',
		'minecraft:oak_stairs',
		'minecraft:pale_oak_stairs',
		'minecraft:spruce_stairs',
		'minecraft:warped_stairs',
	strict=False))