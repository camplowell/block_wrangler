from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:dragon_immune')
	
	tag.add(block_types(
		'minecraft:end_gateway',
		'minecraft:reinforced_deepslate',
		'minecraft:respawn_anchor',
		'minecraft:obsidian',
		'minecraft:end_portal',
		'minecraft:bedrock',
		'minecraft:repeating_command_block',
		'minecraft:moving_piston',
		'minecraft:crying_obsidian',
		'minecraft:barrier',
		'minecraft:structure_block',
		'minecraft:iron_bars',
		'minecraft:chain_command_block',
		'minecraft:end_portal_frame',
		'minecraft:end_stone',
		'minecraft:command_block',
		'minecraft:jigsaw',
	strict=False))