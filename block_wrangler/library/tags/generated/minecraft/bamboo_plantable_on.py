from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:bamboo_plantable_on')
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:sand'))
	
	tag.add(block_types(
		'minecraft:bamboo',
		'minecraft:bamboo_sapling',
		'minecraft:gravel',
		'minecraft:suspicious_gravel',
	strict=False))