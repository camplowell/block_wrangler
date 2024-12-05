from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:snaps_goat_horn')
	tag.add(library.touch('minecraft:overworld_natural_logs'))
	
	tag.add(block_types(
		'minecraft:coal_ore',
		'minecraft:copper_ore',
		'minecraft:emerald_ore',
		'minecraft:iron_ore',
		'minecraft:packed_ice',
		'minecraft:stone',
	strict=False))