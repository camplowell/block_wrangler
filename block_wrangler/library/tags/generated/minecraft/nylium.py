from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:nylium')
	
	tag.add(block_types(
		'minecraft:crimson_nylium',
		'minecraft:warped_nylium',
	strict=False))