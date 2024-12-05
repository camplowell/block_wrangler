from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:stone_pressure_plates')
	
	tag.add(block_types(
		'minecraft:polished_blackstone_pressure_plate',
		'minecraft:stone_pressure_plate',
	strict=False))