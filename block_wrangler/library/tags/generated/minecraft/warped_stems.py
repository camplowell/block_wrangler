from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:warped_stems')
	
	tag.add(block_types(
		'minecraft:stripped_warped_hyphae',
		'minecraft:stripped_warped_stem',
		'minecraft:warped_hyphae',
		'minecraft:warped_stem',
	strict=False))