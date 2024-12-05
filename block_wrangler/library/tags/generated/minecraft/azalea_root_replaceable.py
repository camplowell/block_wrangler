from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:azalea_root_replaceable')
	tag.add(library.touch('minecraft:base_stone_overworld'))
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:terracotta'))
	
	tag.add(block_types(
		'minecraft:clay',
		'minecraft:gravel',
		'minecraft:powder_snow',
		'minecraft:red_sand',
		'minecraft:sand',
		'minecraft:snow_block',
	strict=False))