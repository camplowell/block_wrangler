from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:nether_carver_replaceables')
	tag.add(library.touch('minecraft:nylium'))
	tag.add(library.touch('minecraft:wart_blocks'))
	tag.add(library.touch('minecraft:base_stone_overworld'))
	tag.add(library.touch('minecraft:base_stone_nether'))
	tag.add(library.touch('minecraft:dirt'))
	
	tag.add(block_types(
		'minecraft:soul_soil',
		'minecraft:soul_sand',
	strict=False))