from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:lightning_rods')
	
	tag.add(block_types(
		'minecraft:exposed_lightning_rod',
		'minecraft:lightning_rod',
		'minecraft:oxidized_lightning_rod',
		'minecraft:waxed_exposed_lightning_rod',
		'minecraft:waxed_lightning_rod',
		'minecraft:waxed_oxidized_lightning_rod',
		'minecraft:waxed_weathered_lightning_rod',
		'minecraft:weathered_lightning_rod',
	strict=False))