from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:mangrove_logs_can_grow_through')
	
	tag.add(block_types(
		'minecraft:mangrove_propagule',
		'minecraft:mangrove_leaves',
		'minecraft:muddy_mangrove_roots',
		'minecraft:moss_carpet',
		'minecraft:mangrove_log',
		'minecraft:vine',
		'minecraft:mud',
		'minecraft:mangrove_roots',
	strict=False))