from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:substrate_overworld')
	tag.add(library.touch('minecraft:dirt'))
	tag.add(library.touch('minecraft:grass_blocks'))
	tag.add(library.touch('minecraft:moss_blocks'))
	tag.add(library.touch('minecraft:mud'))
	