from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:pressure_plates')
	tag.add(library.touch('minecraft:wooden_pressure_plates'))
	tag.add(library.touch('minecraft:stone_pressure_plates'))
	
	tag.add(block_types(
		'minecraft:light_weighted_pressure_plate',
		'minecraft:heavy_weighted_pressure_plate',
	strict=False))