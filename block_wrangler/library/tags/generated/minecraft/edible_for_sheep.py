from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:edible_for_sheep')
	
	tag.add(block_types(
		'minecraft:fern',
		'minecraft:short_dry_grass',
		'minecraft:short_grass',
		'minecraft:tall_dry_grass',
	strict=False))