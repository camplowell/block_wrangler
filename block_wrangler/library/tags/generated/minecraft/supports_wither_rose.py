from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_wither_rose')
	tag.add(library.touch('minecraft:supports_vegetation'))
	
	tag.add(block_types(
		'minecraft:netherrack',
		'minecraft:soul_sand',
		'minecraft:soul_soil',
	strict=False))