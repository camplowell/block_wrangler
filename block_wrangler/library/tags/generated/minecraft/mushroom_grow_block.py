from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:mushroom_grow_block')
	
	tag.add(block_types(
		'minecraft:crimson_nylium',
		'minecraft:mycelium',
		'minecraft:podzol',
		'minecraft:warped_nylium',
	strict=False))