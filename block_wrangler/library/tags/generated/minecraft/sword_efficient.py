from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:sword_efficient')
	tag.add(library.touch('minecraft:leaves'))
	tag.add(library.touch('minecraft:crops'))
	tag.add(library.touch('minecraft:saplings'))
	tag.add(library.touch('minecraft:small_flowers'))
	
	tag.add(block_types(
		'minecraft:cave_vines',
		'minecraft:fern',
		'minecraft:lilac',
		'minecraft:twisting_vines_plant',
		'minecraft:chorus_flower',
		'minecraft:spore_blossom',
		'minecraft:big_dripleaf',
		'minecraft:peony',
		'minecraft:carved_pumpkin',
		'minecraft:crimson_roots',
		'minecraft:dead_bush',
		'minecraft:jack_o_lantern',
		'minecraft:big_dripleaf_stem',
		'minecraft:sunflower',
		'minecraft:warped_fungus',
		'minecraft:twisting_vines',
		'minecraft:hanging_roots',
		'minecraft:short_grass',
		'minecraft:warped_roots',
		'minecraft:attached_melon_stem',
		'minecraft:weeping_vines',
		'minecraft:crimson_fungus',
		'minecraft:red_mushroom',
		'minecraft:cocoa',
		'minecraft:pitcher_plant',
		'minecraft:small_dripleaf',
		'minecraft:pink_petals',
		'minecraft:rose_bush',
		'minecraft:nether_sprouts',
		'minecraft:vine',
		'minecraft:melon',
		'minecraft:large_fern',
		'minecraft:attached_pumpkin_stem',
		'minecraft:pitcher_crop',
		'minecraft:sweet_berry_bush',
		'minecraft:sugar_cane',
		'minecraft:cave_vines_plant',
		'minecraft:chorus_plant',
		'minecraft:moss_carpet',
		'minecraft:weeping_vines_plant',
		'minecraft:glow_lichen',
		'minecraft:brown_mushroom',
		'minecraft:pumpkin',
		'minecraft:nether_wart',
		'minecraft:lily_pad',
		'minecraft:tall_grass',
	strict=False))