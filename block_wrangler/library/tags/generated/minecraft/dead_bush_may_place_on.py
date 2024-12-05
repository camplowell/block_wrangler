from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:dead_bush_may_place_on')
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:sand'))
	tag.add(library.touch('minecraft:terracotta'))
	