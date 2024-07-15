from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:vibration_resonators')
	
	tag.add(block_types(
		'minecraft:amethyst_block',
	strict=False))