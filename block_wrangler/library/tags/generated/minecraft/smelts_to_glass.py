from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:smelts_to_glass')
	
	tag.add(block_types(
		'minecraft:red_sand',
		'minecraft:sand',
	strict=False))