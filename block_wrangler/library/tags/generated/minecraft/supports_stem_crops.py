from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_stem_crops')
	tag.add(library.touch('minecraft:supports_crops'))
	