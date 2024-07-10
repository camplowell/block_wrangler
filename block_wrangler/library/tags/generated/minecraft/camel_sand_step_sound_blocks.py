from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:camel_sand_step_sound_blocks')
	tag.add(library.touch('minecraft:concrete_powder'))
	tag.add(library.touch('minecraft:sand'))
	