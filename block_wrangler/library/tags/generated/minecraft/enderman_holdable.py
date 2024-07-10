from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:enderman_holdable')
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:small_flowers'))
	
	tag.add(block_types(
		'minecraft:melon',
		'minecraft:crimson_fungus',
		'minecraft:red_mushroom',
		'minecraft:gravel',
		'minecraft:clay',
		'minecraft:sand',
		'minecraft:cactus',
		'minecraft:crimson_nylium',
		'minecraft:warped_fungus',
		'minecraft:warped_nylium',
		'minecraft:brown_mushroom',
		'minecraft:red_sand',
		'minecraft:pumpkin',
		'minecraft:crimson_roots',
		'minecraft:tnt',
		'minecraft:warped_roots',
		'minecraft:carved_pumpkin',
	strict=False))