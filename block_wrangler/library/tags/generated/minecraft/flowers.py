from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:flowers')
	tag.add(library.touch('minecraft:small_flowers'))
	tag.add(library.touch('minecraft:tall_flowers'))
	
	tag.add(block_types(
		'minecraft:cactus_flower',
		'minecraft:cherry_leaves',
		'minecraft:chorus_flower',
		'minecraft:flowering_azalea',
		'minecraft:flowering_azalea_leaves',
		'minecraft:lilac',
		'minecraft:mangrove_propagule',
		'minecraft:peony',
		'minecraft:pink_petals',
		'minecraft:pitcher_plant',
		'minecraft:rose_bush',
		'minecraft:spore_blossom',
		'minecraft:sunflower',
		'minecraft:wildflowers',
	strict=False))