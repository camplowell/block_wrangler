from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:beneath_tree_podzol_replaceable')
	tag.add(library.touch('minecraft:substrate_overworld'))
	