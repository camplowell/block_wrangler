from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_bamboo')
	tag.add(library.touch('minecraft:sand'))
	tag.add(library.touch('minecraft:substrate_overworld'))
	
	tag.add(block_types(
		'minecraft:bamboo',
		'minecraft:bamboo_sapling',
		'minecraft:gravel',
		'minecraft:suspicious_gravel',
	strict=False))