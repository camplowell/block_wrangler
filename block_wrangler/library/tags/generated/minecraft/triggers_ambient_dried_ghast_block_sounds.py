from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:triggers_ambient_dried_ghast_block_sounds')
	
	tag.add(block_types(
		'minecraft:soul_sand',
		'minecraft:soul_soil',
	strict=False))