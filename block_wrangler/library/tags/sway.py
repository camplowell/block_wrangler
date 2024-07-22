from block_wrangler.tag import Tag, TagLibrary
from block_wrangler.block_type import BlockState
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('sway')

	library.touch('sway/short') \
		.add(library.touch('minecraft:small_flowers')) \
		.add(library.touch('minecraft:saplings')) \
		.add(block_types(
			'minecraft:bamboo_sapling',
			'minecraft:beetroots',
			'minecraft:carrots',
			'minecraft:dead_bush',
			'minecraft:fern',
			'minecraft:melon_stem',
			'minecraft:potatoes',
			'minecraft:pumpkin_stem',
			'minecraft:seagrass',
			'minecraft:short_grass',
			'minecraft:sweet_berry_bush',
			'minecraft:torchflower_crop',
			'minecraft:wheat',
		)) \
		.add(block_types(
			'minecraft:mangrove_propagule'
		), lambda state: state.hanging == 'false')
	
	library.touch('sway/lower') \
		.add(library.touch('plant'), lambda state: state.half == 'lower')
	
	library.touch('sway/upper') \
		.add(library.touch('plant'), lambda state: state.half == 'upper')
	
	library.touch('sway/double') \
		.add(library.touch('plant'), lambda state: state.half != BlockState.MISSING)
	
	library.touch('sway/hanging') \
		.add(block_types(
			'minecraft:hanging_roots'
		)) \
		.add(block_types(
			'minecraft:mangrove_propagule', 
			'minecraft:lantern'
		), lambda state: state.hanging == 'true')

	library.touch('sway/whole') \
		.add(library.touch('minecraft:leaves'))
	
	library.touch('sway/floating') \
		.add(block_types('minecraft:lily_pad'))
	
	library.touch('sway/slow') \
		.set_mode(Tag.WidenedMode(lambda state: state.waterlogged == 'true')) \
		.add(block_types('minecraft:seagrass', 'minecraft:tall_seagrass', 'minecraft:lily_pad'))