from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:rabbits_spawnable_on')
	
	tag.add(block_types(
		'minecraft:snow',
		'minecraft:sand',
		'minecraft:grass_block',
		'minecraft:snow_block',
	strict=False))