from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:does_not_block_hoppers')
	tag.add(library.touch('minecraft:beehives'))
	