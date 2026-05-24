from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:ice_spike_replaceable')
	tag.add(library.touch('minecraft:substrate_overworld'))
	
	tag.add(block_types(
		'minecraft:ice',
		'minecraft:snow_block',
	strict=False))