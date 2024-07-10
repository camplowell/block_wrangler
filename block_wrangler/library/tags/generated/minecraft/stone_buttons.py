from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:stone_buttons')
	
	tag.add(block_types(
		'minecraft:stone_button',
		'minecraft:polished_blackstone_button',
	strict=False))