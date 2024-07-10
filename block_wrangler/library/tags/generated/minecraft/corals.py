from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:corals')
	tag.add(library.touch('minecraft:coral_plants'))
	
	tag.add(block_types(
		'minecraft:fire_coral_fan',
		'minecraft:bubble_coral_fan',
		'minecraft:brain_coral_fan',
		'minecraft:horn_coral_fan',
		'minecraft:tube_coral_fan',
	strict=False))