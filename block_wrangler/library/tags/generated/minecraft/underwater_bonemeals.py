from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:underwater_bonemeals')
	tag.add(library.touch('minecraft:wall_corals'))
	tag.add(library.touch('minecraft:corals'))
	
	tag.add(block_types(
		'minecraft:seagrass',
	strict=False))