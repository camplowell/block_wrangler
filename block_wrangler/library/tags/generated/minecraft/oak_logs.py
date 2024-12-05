from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:oak_logs')
	
	tag.add(block_types(
		'minecraft:oak_log',
		'minecraft:oak_wood',
		'minecraft:stripped_oak_log',
		'minecraft:stripped_oak_wood',
	strict=False))