from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_trapdoors')
	
	tag.add(block_types(
		'minecraft:acacia_trapdoor',
		'minecraft:bamboo_trapdoor',
		'minecraft:birch_trapdoor',
		'minecraft:cherry_trapdoor',
		'minecraft:crimson_trapdoor',
		'minecraft:dark_oak_trapdoor',
		'minecraft:jungle_trapdoor',
		'minecraft:mangrove_trapdoor',
		'minecraft:oak_trapdoor',
		'minecraft:pale_oak_trapdoor',
		'minecraft:spruce_trapdoor',
		'minecraft:warped_trapdoor',
	strict=False))