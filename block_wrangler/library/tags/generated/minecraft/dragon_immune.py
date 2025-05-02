from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:dragon_immune')
	
	tag.add(block_types(
		'minecraft:barrier',
		'minecraft:bedrock',
		'minecraft:chain_command_block',
		'minecraft:command_block',
		'minecraft:crying_obsidian',
		'minecraft:end_gateway',
		'minecraft:end_portal',
		'minecraft:end_portal_frame',
		'minecraft:end_stone',
		'minecraft:iron_bars',
		'minecraft:jigsaw',
		'minecraft:moving_piston',
		'minecraft:obsidian',
		'minecraft:reinforced_deepslate',
		'minecraft:repeating_command_block',
		'minecraft:respawn_anchor',
		'minecraft:structure_block',
		'minecraft:test_block',
		'minecraft:test_instance_block',
	strict=False))