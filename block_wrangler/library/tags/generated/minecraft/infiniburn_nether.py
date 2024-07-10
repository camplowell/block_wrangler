from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:infiniburn_nether')
	tag.add(library.touch('minecraft:infiniburn_overworld'))
	