from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:enderman_holdable')
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:small_flowers'))
	
	tag.add(block_types(
		'minecraft:brown_mushroom',
		'minecraft:cactus',
		'minecraft:carved_pumpkin',
		'minecraft:clay',
		'minecraft:crimson_fungus',
		'minecraft:crimson_nylium',
		'minecraft:crimson_roots',
		'minecraft:gravel',
		'minecraft:melon',
		'minecraft:pumpkin',
		'minecraft:red_mushroom',
		'minecraft:red_sand',
		'minecraft:sand',
		'minecraft:tnt',
		'minecraft:warped_fungus',
		'minecraft:warped_nylium',
		'minecraft:warped_roots',
	strict=False))