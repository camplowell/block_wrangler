from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:logs_that_burn')
	tag.add(library.touch('minecraft:cherry_logs'))
	tag.add(library.touch('minecraft:dark_oak_logs'))
	tag.add(library.touch('minecraft:jungle_logs'))
	tag.add(library.touch('minecraft:spruce_logs'))
	tag.add(library.touch('minecraft:mangrove_logs'))
	tag.add(library.touch('minecraft:acacia_logs'))
	tag.add(library.touch('minecraft:oak_logs'))
	tag.add(library.touch('minecraft:birch_logs'))
	