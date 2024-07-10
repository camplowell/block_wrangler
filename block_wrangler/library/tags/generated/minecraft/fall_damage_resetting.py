from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:fall_damage_resetting')
	tag.add(library.touch('minecraft:climbable'))
	
	tag.add(block_types(
		'minecraft:cobweb',
		'minecraft:sweet_berry_bush',
	strict=False))