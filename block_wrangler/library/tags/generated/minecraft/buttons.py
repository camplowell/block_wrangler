from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:buttons')
	tag.add(library.touch('minecraft:wooden_buttons'))
	tag.add(library.touch('minecraft:stone_buttons'))
	