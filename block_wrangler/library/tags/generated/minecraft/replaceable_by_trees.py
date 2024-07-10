from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:replaceable_by_trees')
	tag.add(library.touch('minecraft:leaves'))
	
	tag.add(block_types(
		'minecraft:fern',
		'minecraft:lilac',
		'minecraft:peony',
		'minecraft:crimson_roots',
		'minecraft:dead_bush',
		'minecraft:sunflower',
		'minecraft:hanging_roots',
		'minecraft:short_grass',
		'minecraft:tall_seagrass',
		'minecraft:warped_roots',
		'minecraft:pitcher_plant',
		'minecraft:rose_bush',
		'minecraft:water',
		'minecraft:nether_sprouts',
		'minecraft:vine',
		'minecraft:large_fern',
		'minecraft:glow_lichen',
		'minecraft:seagrass',
		'minecraft:tall_grass',
	strict=False))