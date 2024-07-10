from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:dripstone_replaceable_blocks')
	tag.add(library.touch('minecraft:base_stone_overworld'))
	