from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:sculk_replaceable')
	tag.add(library.touch('minecraft:base_stone_nether'))
	tag.add(library.touch('minecraft:base_stone_overworld'))
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:nylium'))
	tag.add(library.touch('minecraft:terracotta'))
	
	tag.add(block_types(
		'minecraft:calcite',
		'minecraft:clay',
		'minecraft:dripstone_block',
		'minecraft:end_stone',
		'minecraft:gravel',
		'minecraft:red_sand',
		'minecraft:red_sandstone',
		'minecraft:sand',
		'minecraft:sandstone',
		'minecraft:smooth_basalt',
		'minecraft:soul_sand',
		'minecraft:soul_soil',
	strict=False))