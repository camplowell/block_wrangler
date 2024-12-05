from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wolves_spawnable_on')
	
	tag.add(block_types(
		'minecraft:coarse_dirt',
		'minecraft:grass_block',
		'minecraft:podzol',
		'minecraft:snow',
		'minecraft:snow_block',
	strict=False))