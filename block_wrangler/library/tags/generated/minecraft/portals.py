from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:portals')
	
	tag.add(block_types(
		'minecraft:end_gateway',
		'minecraft:end_portal',
		'minecraft:nether_portal',
	strict=False))