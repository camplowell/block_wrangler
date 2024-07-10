from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:logs')
	tag.add(library.touch('minecraft:warped_stems'))
	tag.add(library.touch('minecraft:logs_that_burn'))
	tag.add(library.touch('minecraft:crimson_stems'))
	