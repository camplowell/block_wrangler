from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:goats_spawnable_on')
	tag.add(library.touch('minecraft:animals_spawnable_on'))
	
	tag.add(block_types(
		'minecraft:snow',
		'minecraft:packed_ice',
		'minecraft:gravel',
		'minecraft:stone',
		'minecraft:snow_block',
	strict=False))