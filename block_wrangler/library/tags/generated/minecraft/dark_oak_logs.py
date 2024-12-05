from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:dark_oak_logs')
	
	tag.add(block_types(
		'minecraft:dark_oak_log',
		'minecraft:dark_oak_wood',
		'minecraft:stripped_dark_oak_log',
		'minecraft:stripped_dark_oak_wood',
	strict=False))