from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:bars')
	
	tag.add(block_types(
		'minecraft:copper_bars',
		'minecraft:exposed_copper_bars',
		'minecraft:iron_bars',
		'minecraft:oxidized_copper_bars',
		'minecraft:waxed_copper_bars',
		'minecraft:waxed_exposed_copper_bars',
		'minecraft:waxed_oxidized_copper_bars',
		'minecraft:waxed_weathered_copper_bars',
		'minecraft:weathered_copper_bars',
	strict=False))