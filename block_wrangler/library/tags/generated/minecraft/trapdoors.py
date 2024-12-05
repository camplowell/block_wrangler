from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:trapdoors')
	tag.add(library.touch('minecraft:wooden_trapdoors'))
	
	tag.add(block_types(
		'minecraft:copper_trapdoor',
		'minecraft:exposed_copper_trapdoor',
		'minecraft:iron_trapdoor',
		'minecraft:oxidized_copper_trapdoor',
		'minecraft:waxed_copper_trapdoor',
		'minecraft:waxed_exposed_copper_trapdoor',
		'minecraft:waxed_oxidized_copper_trapdoor',
		'minecraft:waxed_weathered_copper_trapdoor',
		'minecraft:weathered_copper_trapdoor',
	strict=False))