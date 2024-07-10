from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:occludes_vibration_signals')
	tag.add(library.touch('minecraft:wool'))
	