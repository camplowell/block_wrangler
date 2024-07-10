from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:prevent_mob_spawning_inside')
	tag.add(library.touch('minecraft:rails'))
	