from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:sculk_replaceable_world_gen')
	tag.add(library.touch('minecraft:sculk_replaceable'))
	
	tag.add(block_types(
		'minecraft:deepslate_tiles',
		'minecraft:deepslate_bricks',
		'minecraft:cobbled_deepslate',
		'minecraft:cracked_deepslate_bricks',
		'minecraft:cracked_deepslate_tiles',
		'minecraft:polished_deepslate',
	strict=False))