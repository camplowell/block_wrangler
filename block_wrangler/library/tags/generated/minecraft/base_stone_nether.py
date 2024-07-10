from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:base_stone_nether')
	
	tag.add(block_types(
		'minecraft:blackstone',
		'minecraft:basalt',
		'minecraft:netherrack',
	strict=False))