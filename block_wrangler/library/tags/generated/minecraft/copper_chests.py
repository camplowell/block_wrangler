from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:copper_chests')
	
	tag.add(block_types(
		'minecraft:copper_chest',
		'minecraft:exposed_copper_chest',
		'minecraft:oxidized_copper_chest',
		'minecraft:waxed_copper_chest',
		'minecraft:waxed_exposed_copper_chest',
		'minecraft:waxed_oxidized_copper_chest',
		'minecraft:waxed_weathered_copper_chest',
		'minecraft:weathered_copper_chest',
	strict=False))