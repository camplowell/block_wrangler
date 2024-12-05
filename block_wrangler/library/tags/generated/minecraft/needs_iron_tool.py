from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:needs_iron_tool')
	
	tag.add(block_types(
		'minecraft:deepslate_diamond_ore',
		'minecraft:deepslate_emerald_ore',
		'minecraft:deepslate_gold_ore',
		'minecraft:deepslate_redstone_ore',
		'minecraft:diamond_block',
		'minecraft:diamond_ore',
		'minecraft:emerald_block',
		'minecraft:emerald_ore',
		'minecraft:gold_block',
		'minecraft:gold_ore',
		'minecraft:raw_gold_block',
		'minecraft:redstone_ore',
	strict=False))