from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wither_immune')
	
	tag.add(block_types(
		'minecraft:end_gateway',
		'minecraft:light',
		'minecraft:end_portal',
		'minecraft:bedrock',
		'minecraft:repeating_command_block',
		'minecraft:moving_piston',
		'minecraft:reinforced_deepslate',
		'minecraft:barrier',
		'minecraft:structure_block',
		'minecraft:chain_command_block',
		'minecraft:end_portal_frame',
		'minecraft:command_block',
		'minecraft:jigsaw',
	strict=False))