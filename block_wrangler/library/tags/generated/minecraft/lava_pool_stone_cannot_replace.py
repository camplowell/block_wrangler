from block_wrangler.tag import TagLibrary


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:lava_pool_stone_cannot_replace')
	tag.add(library.touch('minecraft:logs'))
	tag.add(library.touch('minecraft:leaves'))
	tag.add(library.touch('minecraft:features_cannot_replace'))
	