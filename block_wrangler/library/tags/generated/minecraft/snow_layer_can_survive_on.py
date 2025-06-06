from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:snow_layer_can_survive_on')
	
	tag.add(block_types(
		'minecraft:honey_block',
		'minecraft:mud',
		'minecraft:soul_sand',
	strict=False))