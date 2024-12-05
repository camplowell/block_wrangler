from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wall_corals')
	
	tag.add(block_types(
		'minecraft:brain_coral_wall_fan',
		'minecraft:bubble_coral_wall_fan',
		'minecraft:fire_coral_wall_fan',
		'minecraft:horn_coral_wall_fan',
		'minecraft:tube_coral_wall_fan',
	strict=False))