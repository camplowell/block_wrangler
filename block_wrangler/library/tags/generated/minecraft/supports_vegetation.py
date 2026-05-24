from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_vegetation')
	tag.add(library.touch('minecraft:substrate_overworld'))
	
	tag.add(block_types(
		'minecraft:farmland',
	strict=False))