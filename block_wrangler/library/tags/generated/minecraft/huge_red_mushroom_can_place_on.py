from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:huge_red_mushroom_can_place_on')
	tag.add(library.touch('minecraft:substrate_overworld'))
	
	tag.add(block_types(
		'minecraft:crimson_nylium',
		'minecraft:mycelium',
		'minecraft:podzol',
		'minecraft:warped_nylium',
	strict=False))