from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:replaceable_by_trees')
	tag.add(library.touch('minecraft:leaves'))
	tag.add(library.touch('minecraft:small_flowers'))
	
	tag.add(block_types(
		'minecraft:crimson_roots',
		'minecraft:dead_bush',
		'minecraft:fern',
		'minecraft:glow_lichen',
		'minecraft:hanging_roots',
		'minecraft:large_fern',
		'minecraft:lilac',
		'minecraft:nether_sprouts',
		'minecraft:pale_moss_carpet',
		'minecraft:peony',
		'minecraft:pitcher_plant',
		'minecraft:rose_bush',
		'minecraft:seagrass',
		'minecraft:short_grass',
		'minecraft:sunflower',
		'minecraft:tall_grass',
		'minecraft:tall_seagrass',
		'minecraft:vine',
		'minecraft:warped_roots',
		'minecraft:water',
	strict=False))