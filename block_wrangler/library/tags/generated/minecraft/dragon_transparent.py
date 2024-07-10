from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:dragon_transparent')
	tag.add(library.touch('minecraft:fire'))
	
	tag.add(block_types(
		'minecraft:light',
	strict=False))