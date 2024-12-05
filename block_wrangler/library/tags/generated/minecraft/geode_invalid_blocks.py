from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:geode_invalid_blocks')
	
	tag.add(block_types(
		'minecraft:bedrock',
		'minecraft:blue_ice',
		'minecraft:ice',
		'minecraft:lava',
		'minecraft:packed_ice',
		'minecraft:water',
	strict=False))