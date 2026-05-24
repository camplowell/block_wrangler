from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:mud')
	
	tag.add(block_types(
		'minecraft:mud',
		'minecraft:muddy_mangrove_roots',
	strict=False))