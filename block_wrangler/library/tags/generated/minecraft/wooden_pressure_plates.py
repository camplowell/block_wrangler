from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_pressure_plates')
	
	tag.add(block_types(
		'minecraft:acacia_pressure_plate',
		'minecraft:bamboo_pressure_plate',
		'minecraft:birch_pressure_plate',
		'minecraft:cherry_pressure_plate',
		'minecraft:crimson_pressure_plate',
		'minecraft:dark_oak_pressure_plate',
		'minecraft:jungle_pressure_plate',
		'minecraft:mangrove_pressure_plate',
		'minecraft:oak_pressure_plate',
		'minecraft:pale_oak_pressure_plate',
		'minecraft:spruce_pressure_plate',
		'minecraft:warped_pressure_plate',
	strict=False))