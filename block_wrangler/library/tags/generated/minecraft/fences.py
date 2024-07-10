from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:fences')
	tag.add(library.touch('minecraft:wooden_fences'))
	
	tag.add(block_types(
		'minecraft:nether_brick_fence',
	strict=False))