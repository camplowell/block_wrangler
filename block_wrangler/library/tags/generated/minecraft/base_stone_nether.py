from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:base_stone_nether')
	
	tag.add(block_types(
		'minecraft:basalt',
		'minecraft:blackstone',
		'minecraft:netherrack',
	strict=False))