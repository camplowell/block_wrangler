from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:supports_sugar_cane')
	tag.add(library.touch('minecraft:sand'))
	tag.add(library.touch('minecraft:substrate_overworld'))
	