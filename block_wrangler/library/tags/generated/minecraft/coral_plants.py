from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:coral_plants')
	
	tag.add(block_types(
		'minecraft:tube_coral',
		'minecraft:bubble_coral',
		'minecraft:horn_coral',
		'minecraft:fire_coral',
		'minecraft:brain_coral',
	strict=False))