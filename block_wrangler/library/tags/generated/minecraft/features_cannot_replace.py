from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:features_cannot_replace')
	
	tag.add(block_types(
		'minecraft:spawner',
		'minecraft:bedrock',
		'minecraft:vault',
		'minecraft:trial_spawner',
		'minecraft:reinforced_deepslate',
		'minecraft:end_portal_frame',
		'minecraft:chest',
	strict=False))