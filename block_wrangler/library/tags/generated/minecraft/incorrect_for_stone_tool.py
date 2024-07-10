from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:incorrect_for_stone_tool')
	tag.add(library.touch('minecraft:needs_diamond_tool'))
	tag.add(library.touch('minecraft:needs_iron_tool'))
	