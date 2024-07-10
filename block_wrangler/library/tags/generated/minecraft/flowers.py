from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:flowers')
	tag.add(library.touch('minecraft:tall_flowers'))
	tag.add(library.touch('minecraft:small_flowers'))
	
	tag.add(block_types(
		'minecraft:mangrove_propagule',
		'minecraft:chorus_flower',
		'minecraft:spore_blossom',
		'minecraft:flowering_azalea_leaves',
		'minecraft:pink_petals',
		'minecraft:cherry_leaves',
		'minecraft:flowering_azalea',
	strict=False))