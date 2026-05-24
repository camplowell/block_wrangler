from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_chorus_flower')
	
	tag.add(block_types(
		'minecraft:end_stone',
	strict=False))