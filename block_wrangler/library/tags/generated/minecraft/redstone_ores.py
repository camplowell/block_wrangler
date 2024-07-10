from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:redstone_ores')
	
	tag.add(block_types(
		'minecraft:redstone_ore',
		'minecraft:deepslate_redstone_ore',
	strict=False))