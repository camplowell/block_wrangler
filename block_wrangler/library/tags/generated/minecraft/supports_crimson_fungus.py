from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_crimson_fungus')
	tag.add(library.touch('minecraft:supports_warped_fungus'))
	