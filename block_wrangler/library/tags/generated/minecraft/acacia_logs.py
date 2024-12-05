from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:acacia_logs')
	
	tag.add(block_types(
		'minecraft:acacia_log',
		'minecraft:acacia_wood',
		'minecraft:stripped_acacia_log',
		'minecraft:stripped_acacia_wood',
	strict=False))