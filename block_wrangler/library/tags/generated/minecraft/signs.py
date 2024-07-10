from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:signs')
	tag.add(library.touch('minecraft:standing_signs'))
	tag.add(library.touch('minecraft:wall_signs'))
	