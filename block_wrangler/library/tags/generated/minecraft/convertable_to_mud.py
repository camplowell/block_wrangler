from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:convertable_to_mud')
	
	tag.add(block_types(
		'minecraft:coarse_dirt',
		'minecraft:dirt',
		'minecraft:rooted_dirt',
	strict=False))