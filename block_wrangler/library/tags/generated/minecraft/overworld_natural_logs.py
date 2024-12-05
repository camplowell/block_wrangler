from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:overworld_natural_logs')
	
	tag.add(block_types(
		'minecraft:acacia_log',
		'minecraft:birch_log',
		'minecraft:cherry_log',
		'minecraft:dark_oak_log',
		'minecraft:jungle_log',
		'minecraft:mangrove_log',
		'minecraft:oak_log',
		'minecraft:pale_oak_log',
		'minecraft:spruce_log',
	strict=False))