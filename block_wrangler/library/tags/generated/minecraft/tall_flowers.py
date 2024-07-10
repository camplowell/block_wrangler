from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:tall_flowers')
	
	tag.add(block_types(
		'minecraft:lilac',
		'minecraft:sunflower',
		'minecraft:pitcher_plant',
		'minecraft:rose_bush',
		'minecraft:peony',
	strict=False))