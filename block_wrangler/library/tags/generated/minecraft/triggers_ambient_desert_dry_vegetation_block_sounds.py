from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:triggers_ambient_desert_dry_vegetation_block_sounds')
	tag.add(library.touch('minecraft:terracotta'))
	
	tag.add(block_types(
		'minecraft:red_sand',
		'minecraft:sand',
	strict=False))