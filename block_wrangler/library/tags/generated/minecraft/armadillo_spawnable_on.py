from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:armadillo_spawnable_on')
	tag.add(library.touch('minecraft:animals_spawnable_on'))
	tag.add(library.touch('minecraft:badlands_terracotta'))
	
	tag.add(block_types(
		'minecraft:coarse_dirt',
		'minecraft:red_sand',
	strict=False))