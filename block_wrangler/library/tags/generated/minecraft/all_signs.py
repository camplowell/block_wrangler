from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:all_signs')
	tag.add(library.touch('minecraft:all_hanging_signs'))
	tag.add(library.touch('minecraft:signs'))
	