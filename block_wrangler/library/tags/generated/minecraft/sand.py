from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:sand')
	
	tag.add(block_types(
		'minecraft:sand',
		'minecraft:red_sand',
		'minecraft:suspicious_sand',
	strict=False))