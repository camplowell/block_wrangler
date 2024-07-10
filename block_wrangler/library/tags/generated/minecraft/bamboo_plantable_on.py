from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:bamboo_plantable_on')
	tag.add(library.touch('minecraft:sand'))
	tag.add(library.touch('minecraft:dirt'))
	
	tag.add(block_types(
		'minecraft:suspicious_gravel',
		'minecraft:bamboo_sapling',
		'minecraft:bamboo',
		'minecraft:gravel',
	strict=False))