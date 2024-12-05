from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:features_cannot_replace')
	
	tag.add(block_types(
		'minecraft:bedrock',
		'minecraft:chest',
		'minecraft:end_portal_frame',
		'minecraft:reinforced_deepslate',
		'minecraft:spawner',
		'minecraft:trial_spawner',
		'minecraft:vault',
	strict=False))