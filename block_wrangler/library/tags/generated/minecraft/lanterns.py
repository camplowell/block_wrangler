from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:lanterns')
	
	tag.add(block_types(
		'minecraft:copper_lantern',
		'minecraft:exposed_copper_lantern',
		'minecraft:lantern',
		'minecraft:oxidized_copper_lantern',
		'minecraft:soul_lantern',
		'minecraft:waxed_copper_lantern',
		'minecraft:waxed_exposed_copper_lantern',
		'minecraft:waxed_oxidized_copper_lantern',
		'minecraft:waxed_weathered_copper_lantern',
		'minecraft:weathered_copper_lantern',
	strict=False))