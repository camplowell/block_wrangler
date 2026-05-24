from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:moss_blocks')
	
	tag.add(block_types(
		'minecraft:moss_block',
		'minecraft:pale_moss_block',
	strict=False))