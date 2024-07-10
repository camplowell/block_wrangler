from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:bamboo_blocks')
	
	tag.add(block_types(
		'minecraft:bamboo_block',
		'minecraft:stripped_bamboo_block',
	strict=False))