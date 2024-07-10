from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:lapis_ores')
	
	tag.add(block_types(
		'minecraft:lapis_ore',
		'minecraft:deepslate_lapis_ore',
	strict=False))