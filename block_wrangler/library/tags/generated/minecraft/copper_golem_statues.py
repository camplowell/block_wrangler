from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:copper_golem_statues')
	
	tag.add(block_types(
		'minecraft:copper_golem_statue',
		'minecraft:exposed_copper_golem_statue',
		'minecraft:oxidized_copper_golem_statue',
		'minecraft:waxed_copper_golem_statue',
		'minecraft:waxed_exposed_copper_golem_statue',
		'minecraft:waxed_oxidized_copper_golem_statue',
		'minecraft:waxed_weathered_copper_golem_statue',
		'minecraft:weathered_copper_golem_statue',
	strict=False))