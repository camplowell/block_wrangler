from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:badlands_terracotta')
	
	tag.add(block_types(
		'minecraft:yellow_terracotta',
		'minecraft:red_terracotta',
		'minecraft:light_gray_terracotta',
		'minecraft:brown_terracotta',
		'minecraft:orange_terracotta',
		'minecraft:terracotta',
		'minecraft:white_terracotta',
	strict=False))