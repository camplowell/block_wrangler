from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_small_dripleaf')
	
	tag.add(block_types(
		'minecraft:clay',
		'minecraft:moss_block',
	strict=False))