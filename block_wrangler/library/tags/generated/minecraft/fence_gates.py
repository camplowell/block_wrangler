from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:fence_gates')
	
	tag.add(block_types(
		'minecraft:acacia_fence_gate',
		'minecraft:oak_fence_gate',
		'minecraft:bamboo_fence_gate',
		'minecraft:crimson_fence_gate',
		'minecraft:birch_fence_gate',
		'minecraft:spruce_fence_gate',
		'minecraft:mangrove_fence_gate',
		'minecraft:dark_oak_fence_gate',
		'minecraft:warped_fence_gate',
		'minecraft:jungle_fence_gate',
		'minecraft:cherry_fence_gate',
	strict=False))