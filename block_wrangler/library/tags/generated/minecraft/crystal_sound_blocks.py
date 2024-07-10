from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:crystal_sound_blocks')
	
	tag.add(block_types(
		'minecraft:amethyst_block',
		'minecraft:budding_amethyst',
	strict=False))