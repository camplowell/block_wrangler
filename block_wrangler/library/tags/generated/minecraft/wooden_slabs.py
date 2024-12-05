from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_slabs')
	
	tag.add(block_types(
		'minecraft:acacia_slab',
		'minecraft:bamboo_slab',
		'minecraft:birch_slab',
		'minecraft:cherry_slab',
		'minecraft:crimson_slab',
		'minecraft:dark_oak_slab',
		'minecraft:jungle_slab',
		'minecraft:mangrove_slab',
		'minecraft:oak_slab',
		'minecraft:pale_oak_slab',
		'minecraft:spruce_slab',
		'minecraft:warped_slab',
	strict=False))