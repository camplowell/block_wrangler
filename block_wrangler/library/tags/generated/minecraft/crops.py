from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:crops')
	
	tag.add(block_types(
		'minecraft:beetroots',
		'minecraft:carrots',
		'minecraft:melon_stem',
		'minecraft:pitcher_crop',
		'minecraft:potatoes',
		'minecraft:pumpkin_stem',
		'minecraft:torchflower_crop',
		'minecraft:wheat',
	strict=False))