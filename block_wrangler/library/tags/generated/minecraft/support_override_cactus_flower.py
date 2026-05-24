from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:support_override_cactus_flower')
	
	tag.add(block_types(
		'minecraft:cactus',
		'minecraft:farmland',
	strict=False))