from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:replaceable')
	
	tag.add(block_types(
		'minecraft:soul_fire',
		'minecraft:fern',
		'minecraft:cave_air',
		'minecraft:crimson_roots',
		'minecraft:dead_bush',
		'minecraft:snow',
		'minecraft:hanging_roots',
		'minecraft:short_grass',
		'minecraft:tall_seagrass',
		'minecraft:lava',
		'minecraft:bubble_column',
		'minecraft:warped_roots',
		'minecraft:structure_void',
		'minecraft:light',
		'minecraft:air',
		'minecraft:water',
		'minecraft:nether_sprouts',
		'minecraft:vine',
		'minecraft:large_fern',
		'minecraft:void_air',
		'minecraft:glow_lichen',
		'minecraft:fire',
		'minecraft:seagrass',
		'minecraft:tall_grass',
	strict=False))