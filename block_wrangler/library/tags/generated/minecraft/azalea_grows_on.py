from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:azalea_grows_on')
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:terracotta'))
	tag.add(library.touch('minecraft:sand'))
	
	tag.add(block_types(
		'minecraft:powder_snow',
		'minecraft:snow_block',
	strict=False))