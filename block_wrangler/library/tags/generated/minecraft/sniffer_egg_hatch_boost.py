from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:sniffer_egg_hatch_boost')
	
	tag.add(block_types(
		'minecraft:moss_block',
	strict=False))