from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:blocks_wind_charge_explosions')
	
	tag.add(block_types(
		'minecraft:bedrock',
		'minecraft:barrier',
	strict=False))