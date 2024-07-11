from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	library.touch('plant/crops').add(library.touch('minecraft:crops'))
	library.touch('plant/flowers').add(library.touch('minecraft:flowers'))
	library.touch('plant/leaves').add(library.touch('minecraft:leaves'))
	library.touch('plant/flowers/potted').add(library.touch('minecraft:flower_pots'))
	library.touch('plant/saplings').add(library.touch('minecraft:saplings'))

	library.touch('plant/thin') \
		.add(library.touch('minecraft:flowers')) \
		.add(library.touch('minecraft:crops')) \
		.add(library.touch('minecraft:flower_pots')) \
		.add(library.touch('minecraft:saplings')) \
		.add(block_types(
			'minecraft:bamboo',
			'minecraft:bamboo_sapling',
			'minecraft:big_dripleaf',
			'minecraft:big_dripleaf_stem',
			'minecraft:cave_vines',
			'minecraft:dead_bush',
			'minecraft:fern',
			'minecraft:hanging_roots',
			'minecraft:large_fern',
			'minecraft:lily_pad',
			'minecraft:mangrove_propagule',
			'minecraft:mangrove_roots',
			'minecraft:pink_petals',
			'minecraft:pitcher_plant',
			'minecraft:seagrass',
			'minecraft:short_grass',
			'minecraft:small_dripleaf',
			'minecraft:spore_blossom',
			'minecraft:sugar_cane',
			'minecraft:sweet_berry_bush',
			'minecraft:tall_grass',
			'minecraft:vine',
		))
	
	library.touch('plant/thick') \
		.add(library.touch('minecraft:leaves')) \
		.add(block_types(
			'minecraft:azalea',
			'minecraft:cactus',
			'minecraft:carved_pumpkin',
			'minecraft:chorus_flower',
			'minecraft:chorus_plant',
			'minecraft:cocoa',
			'minecraft:flowering_azalea',
			'minecraft:jack_o_lantern',
			'minecraft:melon',
			'minecraft:moss_block',
			'minecraft:moss_carpet',
			'minecraft:pumpkin',
		))
	
	library.touch('plant/stem') \
		.add(block_types(
			'minecraft:dead_bush',
			'minecraft:melon_stem',
			'minecraft:pumpkin_stem',
			'minecraft:mangrove_roots',
		))
