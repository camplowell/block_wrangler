from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:parrots_spawnable_on')
	tag.add(library.touch('minecraft:logs'))
	tag.add(library.touch('minecraft:leaves'))
	
	tag.add(block_types(
		'minecraft:grass_block',
		'minecraft:air',
	strict=False))