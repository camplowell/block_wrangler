from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:needs_stone_tool')
	
	tag.add(block_types(
		'minecraft:waxed_exposed_cut_copper_slab',
		'minecraft:raw_iron_block',
		'minecraft:weathered_cut_copper_slab',
		'minecraft:exposed_cut_copper',
		'minecraft:waxed_oxidized_copper_grate',
		'minecraft:weathered_copper_bulb',
		'minecraft:deepslate_copper_ore',
		'minecraft:waxed_oxidized_chiseled_copper',
		'minecraft:waxed_cut_copper',
		'minecraft:exposed_copper_door',
		'minecraft:waxed_weathered_copper_trapdoor',
		'minecraft:deepslate_lapis_ore',
		'minecraft:oxidized_copper_grate',
		'minecraft:weathered_cut_copper_stairs',
		'minecraft:lapis_block',
		'minecraft:exposed_chiseled_copper',
		'minecraft:waxed_weathered_chiseled_copper',
		'minecraft:iron_ore',
		'minecraft:copper_block',
		'minecraft:lightning_rod',
		'minecraft:waxed_oxidized_cut_copper_stairs',
		'minecraft:oxidized_copper_door',
		'minecraft:exposed_copper_bulb',
		'minecraft:waxed_copper_bulb',
		'minecraft:waxed_exposed_copper',
		'minecraft:waxed_exposed_copper_trapdoor',
		'minecraft:oxidized_copper',
		'minecraft:waxed_oxidized_copper',
		'minecraft:cut_copper',
		'minecraft:waxed_weathered_copper_bulb',
		'minecraft:waxed_cut_copper_slab',
		'minecraft:cut_copper_stairs',
		'minecraft:waxed_oxidized_copper_trapdoor',
		'minecraft:copper_trapdoor',
		'minecraft:iron_block',
		'minecraft:waxed_oxidized_copper_door',
		'minecraft:waxed_oxidized_cut_copper_slab',
		'minecraft:exposed_cut_copper_stairs',
		'minecraft:copper_grate',
		'minecraft:lapis_ore',
		'minecraft:oxidized_cut_copper_slab',
		'minecraft:chiseled_copper',
		'minecraft:waxed_copper_door',
		'minecraft:copper_door',
		'minecraft:waxed_oxidized_copper_bulb',
		'minecraft:weathered_copper_door',
		'minecraft:copper_ore',
		'minecraft:waxed_copper_block',
		'minecraft:exposed_copper_trapdoor',
		'minecraft:waxed_exposed_copper_grate',
		'minecraft:waxed_weathered_cut_copper',
		'minecraft:waxed_exposed_copper_door',
		'minecraft:weathered_copper',
		'minecraft:deepslate_iron_ore',
		'minecraft:waxed_weathered_copper_door',
		'minecraft:oxidized_copper_bulb',
		'minecraft:oxidized_copper_trapdoor',
		'minecraft:waxed_exposed_copper_bulb',
		'minecraft:waxed_weathered_cut_copper_stairs',
		'minecraft:copper_bulb',
		'minecraft:oxidized_cut_copper',
		'minecraft:waxed_weathered_copper_grate',
		'minecraft:exposed_cut_copper_slab',
		'minecraft:waxed_oxidized_cut_copper',
		'minecraft:waxed_exposed_cut_copper',
		'minecraft:exposed_copper',
		'minecraft:waxed_exposed_chiseled_copper',
		'minecraft:raw_copper_block',
		'minecraft:weathered_cut_copper',
		'minecraft:exposed_copper_grate',
		'minecraft:waxed_cut_copper_stairs',
		'minecraft:waxed_chiseled_copper',
		'minecraft:weathered_copper_grate',
		'minecraft:waxed_weathered_copper',
		'minecraft:waxed_weathered_cut_copper_slab',
		'minecraft:crafter',
		'minecraft:waxed_exposed_cut_copper_stairs',
		'minecraft:oxidized_chiseled_copper',
		'minecraft:waxed_copper_grate',
		'minecraft:waxed_copper_trapdoor',
		'minecraft:weathered_chiseled_copper',
		'minecraft:weathered_copper_trapdoor',
		'minecraft:oxidized_cut_copper_stairs',
		'minecraft:cut_copper_slab',
	strict=False))