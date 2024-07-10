from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:trail_ruins_replaceable')
	
	tag.add(block_types(
		'minecraft:gravel',
	strict=False))