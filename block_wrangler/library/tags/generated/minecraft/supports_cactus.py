from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_cactus')
	tag.add(library.touch('minecraft:sand'))
	