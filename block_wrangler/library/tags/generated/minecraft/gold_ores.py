from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:gold_ores')
	
	tag.add(block_types(
		'minecraft:deepslate_gold_ore',
		'minecraft:nether_gold_ore',
		'minecraft:gold_ore',
	strict=False))