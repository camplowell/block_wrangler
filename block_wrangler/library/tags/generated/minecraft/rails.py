from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:rails')
	
	tag.add(block_types(
		'minecraft:activator_rail',
		'minecraft:detector_rail',
		'minecraft:powered_rail',
		'minecraft:rail',
	strict=False))