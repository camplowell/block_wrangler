from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:can_glide_through')
	tag.add(library.touch('minecraft:cave_vines'))
	
	tag.add(block_types(
		'minecraft:twisting_vines',
		'minecraft:twisting_vines_plant',
		'minecraft:vine',
		'minecraft:weeping_vines',
		'minecraft:weeping_vines_plant',
	strict=False))