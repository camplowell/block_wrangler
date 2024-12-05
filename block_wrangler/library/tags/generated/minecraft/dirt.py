from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:dirt')
	
	tag.add(block_types(
		'minecraft:coarse_dirt',
		'minecraft:dirt',
		'minecraft:grass_block',
		'minecraft:moss_block',
		'minecraft:mud',
		'minecraft:muddy_mangrove_roots',
		'minecraft:mycelium',
		'minecraft:pale_moss_block',
		'minecraft:podzol',
		'minecraft:rooted_dirt',
	strict=False))