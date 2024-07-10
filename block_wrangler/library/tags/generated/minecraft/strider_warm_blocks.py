from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:strider_warm_blocks')
	
	tag.add(block_types(
		'minecraft:lava',
	strict=False))