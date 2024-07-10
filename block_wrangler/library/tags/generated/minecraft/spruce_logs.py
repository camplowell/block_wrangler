from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:spruce_logs')
	
	tag.add(block_types(
		'minecraft:stripped_spruce_wood',
		'minecraft:stripped_spruce_log',
		'minecraft:spruce_log',
		'minecraft:spruce_wood',
	strict=False))