from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:coal_ores')
	
	tag.add(block_types(
		'minecraft:deepslate_coal_ore',
		'minecraft:coal_ore',
	strict=False))