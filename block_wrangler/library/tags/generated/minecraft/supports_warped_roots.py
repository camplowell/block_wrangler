from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_warped_roots')
	tag.add(library.touch('minecraft:nylium'))
	tag.add(library.touch('minecraft:supports_vegetation'))
	
	tag.add(block_types(
		'minecraft:soul_soil',
	strict=False))