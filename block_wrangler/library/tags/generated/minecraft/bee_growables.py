from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:bee_growables')
	tag.add(library.touch('minecraft:crops'))
	
	tag.add(block_types(
		'minecraft:cave_vines',
		'minecraft:cave_vines_plant',
		'minecraft:sweet_berry_bush',
	strict=False))