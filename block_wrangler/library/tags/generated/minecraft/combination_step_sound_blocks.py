from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:combination_step_sound_blocks')
	tag.add(library.touch('minecraft:wool_carpets'))
	
	tag.add(block_types(
		'minecraft:snow',
		'minecraft:moss_carpet',
		'minecraft:warped_roots',
		'minecraft:crimson_roots',
		'minecraft:nether_sprouts',
	strict=False))