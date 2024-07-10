from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:geode_invalid_blocks')
	
	tag.add(block_types(
		'minecraft:packed_ice',
		'minecraft:ice',
		'minecraft:blue_ice',
		'minecraft:bedrock',
		'minecraft:lava',
		'minecraft:water',
	strict=False))