from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:sword_instantly_mines')
	
	tag.add(block_types(
		'minecraft:bamboo',
		'minecraft:bamboo_sapling',
	strict=False))