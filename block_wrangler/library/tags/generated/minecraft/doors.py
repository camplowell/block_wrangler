from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:doors')
	tag.add(library.touch('minecraft:wooden_doors'))
	
	tag.add(block_types(
		'minecraft:waxed_oxidized_copper_door',
		'minecraft:oxidized_copper_door',
		'minecraft:exposed_copper_door',
		'minecraft:waxed_weathered_copper_door',
		'minecraft:waxed_copper_door',
		'minecraft:iron_door',
		'minecraft:copper_door',
		'minecraft:weathered_copper_door',
		'minecraft:waxed_exposed_copper_door',
	strict=False))