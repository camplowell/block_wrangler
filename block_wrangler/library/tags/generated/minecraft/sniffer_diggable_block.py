from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:sniffer_diggable_block')
	
	tag.add(block_types(
		'minecraft:grass_block',
		'minecraft:podzol',
		'minecraft:muddy_mangrove_roots',
		'minecraft:rooted_dirt',
		'minecraft:coarse_dirt',
		'minecraft:moss_block',
		'minecraft:mud',
		'minecraft:dirt',
	strict=False))