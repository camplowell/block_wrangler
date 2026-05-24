from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:cannot_replace_below_tree_trunk')
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:moss_blocks'))
	tag.add(library.touch('minecraft:mud'))
	
	tag.add(block_types(
		'minecraft:podzol',
	strict=False))