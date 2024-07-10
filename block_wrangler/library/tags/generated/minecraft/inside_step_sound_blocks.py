from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:inside_step_sound_blocks')
	
	tag.add(block_types(
		'minecraft:pink_petals',
		'minecraft:glow_lichen',
		'minecraft:lily_pad',
		'minecraft:small_amethyst_bud',
		'minecraft:sculk_vein',
		'minecraft:powder_snow',
	strict=False))