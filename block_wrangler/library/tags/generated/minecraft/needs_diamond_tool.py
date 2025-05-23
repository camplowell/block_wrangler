from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:needs_diamond_tool')
	
	tag.add(block_types(
		'minecraft:ancient_debris',
		'minecraft:crying_obsidian',
		'minecraft:netherite_block',
		'minecraft:obsidian',
		'minecraft:respawn_anchor',
	strict=False))