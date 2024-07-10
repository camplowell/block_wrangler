from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:crops')
	
	tag.add(block_types(
		'minecraft:pitcher_crop',
		'minecraft:melon_stem',
		'minecraft:potatoes',
		'minecraft:pumpkin_stem',
		'minecraft:wheat',
		'minecraft:carrots',
		'minecraft:torchflower_crop',
		'minecraft:beetroots',
	strict=False))