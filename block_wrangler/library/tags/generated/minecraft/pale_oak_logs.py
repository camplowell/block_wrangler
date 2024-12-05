from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:pale_oak_logs')
	
	tag.add(block_types(
		'minecraft:pale_oak_log',
		'minecraft:pale_oak_wood',
		'minecraft:stripped_pale_oak_log',
		'minecraft:stripped_pale_oak_wood',
	strict=False))