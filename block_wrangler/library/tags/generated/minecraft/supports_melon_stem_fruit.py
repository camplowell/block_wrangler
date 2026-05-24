from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_melon_stem_fruit')
	tag.add(library.touch('minecraft:supports_stem_fruit'))
	