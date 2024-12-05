from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:maintains_farmland')
	
	tag.add(block_types(
		'minecraft:attached_melon_stem',
		'minecraft:attached_pumpkin_stem',
		'minecraft:beetroots',
		'minecraft:carrots',
		'minecraft:melon_stem',
		'minecraft:pitcher_crop',
		'minecraft:potatoes',
		'minecraft:pumpkin_stem',
		'minecraft:torchflower',
		'minecraft:torchflower_crop',
		'minecraft:wheat',
	strict=False))