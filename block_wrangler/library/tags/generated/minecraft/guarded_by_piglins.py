from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:guarded_by_piglins')
	tag.add(library.touch('minecraft:gold_ores'))
	tag.add(library.touch('minecraft:shulker_boxes'))
	
	tag.add(block_types(
		'minecraft:barrel',
		'minecraft:chest',
		'minecraft:ender_chest',
		'minecraft:gilded_blackstone',
		'minecraft:gold_block',
		'minecraft:raw_gold_block',
		'minecraft:trapped_chest',
	strict=False))