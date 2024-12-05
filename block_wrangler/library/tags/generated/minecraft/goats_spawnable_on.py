from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:goats_spawnable_on')
	tag.add(library.touch('minecraft:animals_spawnable_on'))
	
	tag.add(block_types(
		'minecraft:gravel',
		'minecraft:packed_ice',
		'minecraft:snow',
		'minecraft:snow_block',
		'minecraft:stone',
	strict=False))