from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:enchantment_power_transmitter')
	tag.add(library.touch('minecraft:replaceable'))
	