from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:polar_bears_spawnable_on_alternate')
	
	tag.add(block_types(
		'minecraft:ice',
	strict=False))