from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:foxes_spawnable_on')
	
	tag.add(block_types(
		'minecraft:snow',
		'minecraft:grass_block',
		'minecraft:podzol',
		'minecraft:coarse_dirt',
		'minecraft:snow_block',
	strict=False))