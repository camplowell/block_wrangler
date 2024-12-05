from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:mineable/shovel')
	tag.add(library.touch('minecraft:concrete_powder'))
	
	tag.add(block_types(
		'minecraft:clay',
		'minecraft:coarse_dirt',
		'minecraft:dirt',
		'minecraft:dirt_path',
		'minecraft:farmland',
		'minecraft:grass_block',
		'minecraft:gravel',
		'minecraft:mud',
		'minecraft:muddy_mangrove_roots',
		'minecraft:mycelium',
		'minecraft:podzol',
		'minecraft:red_sand',
		'minecraft:rooted_dirt',
		'minecraft:sand',
		'minecraft:snow',
		'minecraft:snow_block',
		'minecraft:soul_sand',
		'minecraft:soul_soil',
		'minecraft:suspicious_gravel',
		'minecraft:suspicious_sand',
	strict=False))