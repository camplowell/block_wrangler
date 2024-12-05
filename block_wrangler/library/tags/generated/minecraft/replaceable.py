from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:replaceable')
	
	tag.add(block_types(
		'minecraft:air',
		'minecraft:bubble_column',
		'minecraft:cave_air',
		'minecraft:crimson_roots',
		'minecraft:dead_bush',
		'minecraft:fern',
		'minecraft:fire',
		'minecraft:glow_lichen',
		'minecraft:hanging_roots',
		'minecraft:large_fern',
		'minecraft:lava',
		'minecraft:light',
		'minecraft:nether_sprouts',
		'minecraft:resin_clump',
		'minecraft:seagrass',
		'minecraft:short_grass',
		'minecraft:snow',
		'minecraft:soul_fire',
		'minecraft:structure_void',
		'minecraft:tall_grass',
		'minecraft:tall_seagrass',
		'minecraft:vine',
		'minecraft:void_air',
		'minecraft:warped_roots',
		'minecraft:water',
	strict=False))