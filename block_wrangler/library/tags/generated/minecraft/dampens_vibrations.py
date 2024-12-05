from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:dampens_vibrations')
	tag.add(library.touch('minecraft:wool'))
	tag.add(library.touch('minecraft:wool_carpets'))
	