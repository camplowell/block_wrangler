from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:sculk_replaceable')
	tag.add(library.touch('minecraft:nylium'))
	tag.add(library.touch('minecraft:base_stone_overworld'))
	tag.add(library.touch('minecraft:base_stone_nether'))
	tag.add(library.touch('minecraft:terracotta'))
	tag.add(library.touch('minecraft:dirt'))
	
	tag.add(block_types(
		'minecraft:sandstone',
		'minecraft:soul_sand',
		'minecraft:gravel',
		'minecraft:clay',
		'minecraft:sand',
		'minecraft:dripstone_block',
		'minecraft:calcite',
		'minecraft:red_sandstone',
		'minecraft:red_sand',
		'minecraft:smooth_basalt',
		'minecraft:end_stone',
		'minecraft:soul_soil',
	strict=False))