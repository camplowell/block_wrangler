from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:unstable_bottom_center')
	tag.add(library.touch('minecraft:fence_gates'))
	