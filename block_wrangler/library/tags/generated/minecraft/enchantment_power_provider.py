from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:enchantment_power_provider')
	
	tag.add(block_types(
		'minecraft:bookshelf',
	strict=False))