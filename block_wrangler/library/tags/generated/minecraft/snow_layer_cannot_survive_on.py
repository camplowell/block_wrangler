from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:snow_layer_cannot_survive_on')
	
	tag.add(block_types(
		'minecraft:barrier',
		'minecraft:ice',
		'minecraft:packed_ice',
	strict=False))