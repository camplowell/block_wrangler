from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:dry_vegetation_may_place_on')
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:sand'))
	tag.add(library.touch('minecraft:terracotta'))
	
	tag.add(block_types(
		'minecraft:farmland',
	strict=False))