from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_trapdoors')
	
	tag.add(block_types(
		'minecraft:warped_trapdoor',
		'minecraft:acacia_trapdoor',
		'minecraft:spruce_trapdoor',
		'minecraft:crimson_trapdoor',
		'minecraft:jungle_trapdoor',
		'minecraft:bamboo_trapdoor',
		'minecraft:birch_trapdoor',
		'minecraft:cherry_trapdoor',
		'minecraft:oak_trapdoor',
		'minecraft:dark_oak_trapdoor',
		'minecraft:mangrove_trapdoor',
	strict=False))