from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:prevents_nearby_leaf_decay')
	tag.add(library.touch('minecraft:logs'))
	