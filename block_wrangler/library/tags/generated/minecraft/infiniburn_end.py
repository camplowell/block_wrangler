from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:infiniburn_end')
	tag.add(library.touch('minecraft:infiniburn_overworld'))
	
	tag.add(block_types(
		'minecraft:bedrock',
	strict=False))