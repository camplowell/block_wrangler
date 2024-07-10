from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:overworld_natural_logs')
	
	tag.add(block_types(
		'minecraft:dark_oak_log',
		'minecraft:mangrove_log',
		'minecraft:cherry_log',
		'minecraft:jungle_log',
		'minecraft:birch_log',
		'minecraft:acacia_log',
		'minecraft:spruce_log',
		'minecraft:oak_log',
	strict=False))