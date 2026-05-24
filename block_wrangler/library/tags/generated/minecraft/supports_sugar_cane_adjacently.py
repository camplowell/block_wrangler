from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_sugar_cane_adjacently')
	
	tag.add(block_types(
		'minecraft:frosted_ice',
	strict=False))