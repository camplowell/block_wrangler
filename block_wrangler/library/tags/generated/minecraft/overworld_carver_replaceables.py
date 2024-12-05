from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:overworld_carver_replaceables')
	tag.add(library.touch('minecraft:base_stone_overworld'))
	tag.add(library.touch('minecraft:copper_ores'))
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:iron_ores'))
	tag.add(library.touch('minecraft:sand'))
	tag.add(library.touch('minecraft:snow'))
	tag.add(library.touch('minecraft:terracotta'))
	
	tag.add(block_types(
		'minecraft:calcite',
		'minecraft:gravel',
		'minecraft:packed_ice',
		'minecraft:raw_copper_block',
		'minecraft:raw_iron_block',
		'minecraft:red_sandstone',
		'minecraft:sandstone',
		'minecraft:snow',
		'minecraft:suspicious_gravel',
		'minecraft:water',
	strict=False))