from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:combination_step_sound_blocks')
	tag.add(library.touch('minecraft:wool_carpets'))
	
	tag.add(block_types(
		'minecraft:crimson_roots',
		'minecraft:moss_carpet',
		'minecraft:nether_sprouts',
		'minecraft:pale_moss_carpet',
		'minecraft:resin_clump',
		'minecraft:snow',
		'minecraft:warped_roots',
	strict=False))