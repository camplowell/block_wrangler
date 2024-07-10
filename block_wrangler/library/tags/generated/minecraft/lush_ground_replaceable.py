from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:lush_ground_replaceable')
	tag.add(library.touch('minecraft:moss_replaceable'))
	
	tag.add(block_types(
		'minecraft:gravel',
		'minecraft:sand',
		'minecraft:clay',
	strict=False))