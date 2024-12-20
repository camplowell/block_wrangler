from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:leaves')
	
	tag.add(block_types(
		'minecraft:acacia_leaves',
		'minecraft:azalea_leaves',
		'minecraft:birch_leaves',
		'minecraft:cherry_leaves',
		'minecraft:dark_oak_leaves',
		'minecraft:flowering_azalea_leaves',
		'minecraft:jungle_leaves',
		'minecraft:mangrove_leaves',
		'minecraft:oak_leaves',
		'minecraft:pale_oak_leaves',
		'minecraft:spruce_leaves',
	strict=False))