from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:mangrove_logs')
	
	tag.add(block_types(
		'minecraft:mangrove_log',
		'minecraft:mangrove_wood',
		'minecraft:stripped_mangrove_log',
		'minecraft:stripped_mangrove_wood',
	strict=False))