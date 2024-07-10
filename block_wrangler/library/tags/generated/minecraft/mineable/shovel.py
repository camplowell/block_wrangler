from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:mineable/shovel')
	tag.add(library.touch('minecraft:concrete_powder'))
	
	tag.add(block_types(
		'minecraft:suspicious_sand',
		'minecraft:farmland',
		'minecraft:soul_soil',
		'minecraft:snow',
		'minecraft:grass_block',
		'minecraft:soul_sand',
		'minecraft:mud',
		'minecraft:dirt_path',
		'minecraft:podzol',
		'minecraft:muddy_mangrove_roots',
		'minecraft:clay',
		'minecraft:gravel',
		'minecraft:rooted_dirt',
		'minecraft:sand',
		'minecraft:coarse_dirt',
		'minecraft:red_sand',
		'minecraft:suspicious_gravel',
		'minecraft:dirt',
		'minecraft:mycelium',
		'minecraft:snow_block',
	strict=False))