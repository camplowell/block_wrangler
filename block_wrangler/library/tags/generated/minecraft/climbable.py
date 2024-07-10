from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:climbable')
	
	tag.add(block_types(
		'minecraft:twisting_vines_plant',
		'minecraft:cave_vines',
		'minecraft:weeping_vines',
		'minecraft:ladder',
		'minecraft:cave_vines_plant',
		'minecraft:weeping_vines_plant',
		'minecraft:twisting_vines',
		'minecraft:scaffolding',
		'minecraft:vine',
	strict=False))