from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:coral_blocks')
	
	tag.add(block_types(
		'minecraft:horn_coral_block',
		'minecraft:brain_coral_block',
		'minecraft:tube_coral_block',
		'minecraft:fire_coral_block',
		'minecraft:bubble_coral_block',
	strict=False))