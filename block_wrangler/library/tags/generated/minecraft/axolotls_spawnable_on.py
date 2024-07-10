from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:axolotls_spawnable_on')
	
	tag.add(block_types(
		'minecraft:clay',
	strict=False))