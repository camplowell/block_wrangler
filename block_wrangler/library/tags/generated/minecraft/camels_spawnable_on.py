from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:camels_spawnable_on')
	tag.add(library.touch('minecraft:sand'))
	