from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:anvil')
	
	tag.add(block_types(
		'minecraft:anvil',
		'minecraft:chipped_anvil',
		'minecraft:damaged_anvil',
	strict=False))