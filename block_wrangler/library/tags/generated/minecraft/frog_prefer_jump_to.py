from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:frog_prefer_jump_to')
	
	tag.add(block_types(
		'minecraft:big_dripleaf',
		'minecraft:lily_pad',
	strict=False))