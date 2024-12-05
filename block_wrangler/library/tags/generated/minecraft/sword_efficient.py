from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:sword_efficient')
	tag.add(library.touch('minecraft:crops'))
	tag.add(library.touch('minecraft:leaves'))
	tag.add(library.touch('minecraft:saplings'))
	tag.add(library.touch('minecraft:small_flowers'))
	
	tag.add(block_types(
		'minecraft:attached_melon_stem',
		'minecraft:attached_pumpkin_stem',
		'minecraft:big_dripleaf',
		'minecraft:big_dripleaf_stem',
		'minecraft:brown_mushroom',
		'minecraft:carved_pumpkin',
		'minecraft:cave_vines',
		'minecraft:cave_vines_plant',
		'minecraft:chorus_flower',
		'minecraft:chorus_plant',
		'minecraft:cocoa',
		'minecraft:crimson_fungus',
		'minecraft:crimson_roots',
		'minecraft:dead_bush',
		'minecraft:fern',
		'minecraft:glow_lichen',
		'minecraft:hanging_roots',
		'minecraft:jack_o_lantern',
		'minecraft:large_fern',
		'minecraft:lilac',
		'minecraft:lily_pad',
		'minecraft:melon',
		'minecraft:moss_carpet',
		'minecraft:nether_sprouts',
		'minecraft:nether_wart',
		'minecraft:peony',
		'minecraft:pink_petals',
		'minecraft:pitcher_crop',
		'minecraft:pitcher_plant',
		'minecraft:pumpkin',
		'minecraft:red_mushroom',
		'minecraft:rose_bush',
		'minecraft:short_grass',
		'minecraft:small_dripleaf',
		'minecraft:spore_blossom',
		'minecraft:sugar_cane',
		'minecraft:sunflower',
		'minecraft:sweet_berry_bush',
		'minecraft:tall_grass',
		'minecraft:twisting_vines',
		'minecraft:twisting_vines_plant',
		'minecraft:vine',
		'minecraft:warped_fungus',
		'minecraft:warped_roots',
		'minecraft:weeping_vines',
		'minecraft:weeping_vines_plant',
	strict=False))