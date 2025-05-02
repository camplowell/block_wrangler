from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wall_post_override')
	tag.add(library.touch('minecraft:banners'))
	tag.add(library.touch('minecraft:pressure_plates'))
	tag.add(library.touch('minecraft:signs'))
	
	tag.add(block_types(
		'minecraft:cactus_flower',
		'minecraft:redstone_torch',
		'minecraft:soul_torch',
		'minecraft:torch',
		'minecraft:tripwire',
	strict=False))