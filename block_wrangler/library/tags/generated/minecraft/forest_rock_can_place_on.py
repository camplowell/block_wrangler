from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:forest_rock_can_place_on')
	tag.add(library.touch('minecraft:base_stone_overworld'))
	tag.add(library.touch('minecraft:substrate_overworld'))
	