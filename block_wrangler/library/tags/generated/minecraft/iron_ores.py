from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:iron_ores')
	
	tag.add(block_types(
		'minecraft:deepslate_iron_ore',
		'minecraft:iron_ore',
	strict=False))