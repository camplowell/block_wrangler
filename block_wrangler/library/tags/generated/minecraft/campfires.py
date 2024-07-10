from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:campfires')
	
	tag.add(block_types(
		'minecraft:soul_campfire',
		'minecraft:campfire',
	strict=False))