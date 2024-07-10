from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:cave_vines')
	
	tag.add(block_types(
		'minecraft:cave_vines',
		'minecraft:cave_vines_plant',
	strict=False))