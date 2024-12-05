from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:inside_step_sound_blocks')
	
	tag.add(block_types(
		'minecraft:glow_lichen',
		'minecraft:lily_pad',
		'minecraft:pink_petals',
		'minecraft:powder_snow',
		'minecraft:sculk_vein',
		'minecraft:small_amethyst_bud',
	strict=False))