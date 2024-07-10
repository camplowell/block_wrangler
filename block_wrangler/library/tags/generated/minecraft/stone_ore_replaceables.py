from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:stone_ore_replaceables')
	
	tag.add(block_types(
		'minecraft:diorite',
		'minecraft:andesite',
		'minecraft:granite',
		'minecraft:stone',
	strict=False))