from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:moss_replaceable')
	tag.add(library.touch('minecraft:cave_vines'))
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:base_stone_overworld'))
	