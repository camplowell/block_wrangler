from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:hoglin_repellents')
	
	tag.add(block_types(
		'minecraft:nether_portal',
		'minecraft:potted_warped_fungus',
		'minecraft:respawn_anchor',
		'minecraft:warped_fungus',
	strict=False))