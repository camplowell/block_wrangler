from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:bats_spawnable_on')
	tag.add(library.touch('minecraft:base_stone_overworld'))
	