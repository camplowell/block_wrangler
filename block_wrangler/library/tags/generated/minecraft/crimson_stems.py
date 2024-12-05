from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:crimson_stems')
	
	tag.add(block_types(
		'minecraft:crimson_hyphae',
		'minecraft:crimson_stem',
		'minecraft:stripped_crimson_hyphae',
		'minecraft:stripped_crimson_stem',
	strict=False))