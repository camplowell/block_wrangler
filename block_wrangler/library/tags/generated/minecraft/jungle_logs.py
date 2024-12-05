from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:jungle_logs')
	
	tag.add(block_types(
		'minecraft:jungle_log',
		'minecraft:jungle_wood',
		'minecraft:stripped_jungle_log',
		'minecraft:stripped_jungle_wood',
	strict=False))