from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:deepslate_ore_replaceables')
	
	tag.add(block_types(
		'minecraft:tuff',
		'minecraft:deepslate',
	strict=False))