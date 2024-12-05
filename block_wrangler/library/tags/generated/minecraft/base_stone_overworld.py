from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:base_stone_overworld')
	
	tag.add(block_types(
		'minecraft:andesite',
		'minecraft:deepslate',
		'minecraft:diorite',
		'minecraft:granite',
		'minecraft:stone',
		'minecraft:tuff',
	strict=False))