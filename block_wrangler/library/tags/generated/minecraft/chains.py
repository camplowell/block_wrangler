from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:chains')
	
	tag.add(block_types(
		'minecraft:copper_chain',
		'minecraft:exposed_copper_chain',
		'minecraft:iron_chain',
		'minecraft:oxidized_copper_chain',
		'minecraft:waxed_copper_chain',
		'minecraft:waxed_exposed_copper_chain',
		'minecraft:waxed_oxidized_copper_chain',
		'minecraft:waxed_weathered_copper_chain',
		'minecraft:weathered_copper_chain',
	strict=False))