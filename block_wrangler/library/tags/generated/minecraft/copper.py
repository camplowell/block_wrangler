from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:copper')
	
	tag.add(block_types(
		'minecraft:copper_block',
		'minecraft:exposed_copper',
		'minecraft:oxidized_copper',
		'minecraft:waxed_copper_block',
		'minecraft:waxed_exposed_copper',
		'minecraft:waxed_oxidized_copper',
		'minecraft:waxed_weathered_copper',
		'minecraft:weathered_copper',
	strict=False))