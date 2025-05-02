from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:big_dripleaf_placeable')
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:small_dripleaf_placeable'))
	
	tag.add(block_types(
		'minecraft:coarse_dirt',
		'minecraft:dirt',
		'minecraft:farmland',
		'minecraft:grass_block',
		'minecraft:moss_block',
		'minecraft:mud',
		'minecraft:muddy_mangrove_roots',
		'minecraft:mycelium',
		'minecraft:podzol',
		'minecraft:rooted_dirt',
	strict=False))