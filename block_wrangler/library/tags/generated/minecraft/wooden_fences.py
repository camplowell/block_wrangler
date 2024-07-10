from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_fences')
	
	tag.add(block_types(
		'minecraft:crimson_fence',
		'minecraft:cherry_fence',
		'minecraft:acacia_fence',
		'minecraft:mangrove_fence',
		'minecraft:warped_fence',
		'minecraft:bamboo_fence',
		'minecraft:oak_fence',
		'minecraft:jungle_fence',
		'minecraft:dark_oak_fence',
		'minecraft:birch_fence',
		'minecraft:spruce_fence',
	strict=False))