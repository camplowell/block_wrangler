from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:enables_bubble_column_push_up')
	
	tag.add(block_types(
		'minecraft:soul_sand',
	strict=False))