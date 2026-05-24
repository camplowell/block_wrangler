from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_dry_vegetation')
	tag.add(library.touch('minecraft:sand'))
	tag.add(library.touch('minecraft:supports_vegetation'))
	tag.add(library.touch('minecraft:terracotta'))
	