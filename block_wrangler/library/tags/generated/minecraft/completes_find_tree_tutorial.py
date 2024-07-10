from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:completes_find_tree_tutorial')
	tag.add(library.touch('minecraft:logs'))
	tag.add(library.touch('minecraft:leaves'))
	tag.add(library.touch('minecraft:wart_blocks'))
	