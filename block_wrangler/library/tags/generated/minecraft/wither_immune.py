from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wither_immune')
	
	tag.add(block_types(
		'minecraft:barrier',
		'minecraft:bedrock',
		'minecraft:chain_command_block',
		'minecraft:command_block',
		'minecraft:end_gateway',
		'minecraft:end_portal',
		'minecraft:end_portal_frame',
		'minecraft:jigsaw',
		'minecraft:light',
		'minecraft:moving_piston',
		'minecraft:reinforced_deepslate',
		'minecraft:repeating_command_block',
		'minecraft:structure_block',
	strict=False))