from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:diamond_ores')
	
	tag.add(block_types(
		'minecraft:diamond_ore',
		'minecraft:deepslate_diamond_ore',
	strict=False))