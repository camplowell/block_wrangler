from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:copper_ores')
	
	tag.add(block_types(
		'minecraft:copper_ore',
		'minecraft:deepslate_copper_ore',
	strict=False))