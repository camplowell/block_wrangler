from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:overworld_carver_replaceables')
	tag.add(library.touch('minecraft:iron_ores'))
	tag.add(library.touch('minecraft:copper_ores'))
	tag.add(library.touch('minecraft:sand'))
	tag.add(library.touch('minecraft:base_stone_overworld'))
	tag.add(library.touch('minecraft:terracotta'))
	tag.add(library.touch('minecraft:dirt'))
	
	tag.add(block_types(
		'minecraft:snow',
		'minecraft:sandstone',
		'minecraft:packed_ice',
		'minecraft:gravel',
		'minecraft:raw_copper_block',
		'minecraft:calcite',
		'minecraft:red_sandstone',
		'minecraft:raw_iron_block',
		'minecraft:suspicious_gravel',
		'minecraft:water',
	strict=False))