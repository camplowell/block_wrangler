from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:coral_plants')
	
	tag.add(block_types(
		'minecraft:brain_coral',
		'minecraft:bubble_coral',
		'minecraft:fire_coral',
		'minecraft:horn_coral',
		'minecraft:tube_coral',
	strict=False))