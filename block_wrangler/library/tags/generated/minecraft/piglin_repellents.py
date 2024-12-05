from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:piglin_repellents')
	
	tag.add(block_types(
		'minecraft:soul_campfire',
		'minecraft:soul_fire',
		'minecraft:soul_lantern',
		'minecraft:soul_torch',
		'minecraft:soul_wall_torch',
	strict=False))