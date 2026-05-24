from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:support_override_snow_layer')
	
	tag.add(block_types(
		'minecraft:honey_block',
		'minecraft:mud',
		'minecraft:soul_sand',
	strict=False))