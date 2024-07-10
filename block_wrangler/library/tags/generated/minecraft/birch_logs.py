from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:birch_logs')
	
	tag.add(block_types(
		'minecraft:stripped_birch_log',
		'minecraft:birch_wood',
		'minecraft:birch_log',
		'minecraft:stripped_birch_wood',
	strict=False))