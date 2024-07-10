from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:cauldrons')
	
	tag.add(block_types(
		'minecraft:powder_snow_cauldron',
		'minecraft:lava_cauldron',
		'minecraft:cauldron',
		'minecraft:water_cauldron',
	strict=False))