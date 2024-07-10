from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:emerald_ores')
	
	tag.add(block_types(
		'minecraft:emerald_ore',
		'minecraft:deepslate_emerald_ore',
	strict=False))