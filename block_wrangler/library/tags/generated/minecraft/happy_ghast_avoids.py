from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:happy_ghast_avoids')
	
	tag.add(block_types(
		'minecraft:cactus',
		'minecraft:fire',
		'minecraft:magma_block',
		'minecraft:pointed_dripstone',
		'minecraft:sweet_berry_bush',
		'minecraft:wither_rose',
	strict=False))