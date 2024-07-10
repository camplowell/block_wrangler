from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:cherry_logs')
	
	tag.add(block_types(
		'minecraft:cherry_log',
		'minecraft:stripped_cherry_log',
		'minecraft:stripped_cherry_wood',
		'minecraft:cherry_wood',
	strict=False))