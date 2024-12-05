from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:invalid_spawn_inside')
	
	tag.add(block_types(
		'minecraft:end_gateway',
		'minecraft:end_portal',
	strict=False))