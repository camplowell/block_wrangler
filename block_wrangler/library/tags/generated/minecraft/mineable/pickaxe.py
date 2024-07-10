from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:mineable/pickaxe')
	tag.add(library.touch('minecraft:cauldrons'))
	tag.add(library.touch('minecraft:shulker_boxes'))
	tag.add(library.touch('minecraft:stone_buttons'))
	tag.add(library.touch('minecraft:walls'))
	tag.add(library.touch('minecraft:rails'))
	tag.add(library.touch('minecraft:anvil'))
	
	tag.add(block_types(
		'minecraft:dispenser',
		'minecraft:smoker',
		'minecraft:raw_gold_block',
		'minecraft:chiseled_polished_blackstone',
		'minecraft:chiseled_quartz_block',
		'minecraft:brown_terracotta',
		'minecraft:green_glazed_terracotta',
		'minecraft:waxed_cut_copper',
		'minecraft:infested_cobblestone',
		'minecraft:infested_mossy_stone_bricks',
		'minecraft:waxed_weathered_copper_trapdoor',
		'minecraft:chiseled_sandstone',
		'minecraft:light_blue_concrete',
		'minecraft:polished_blackstone_pressure_plate',
		'minecraft:dropper',
		'minecraft:oxidized_copper_grate',
		'minecraft:quartz_block',
		'minecraft:weathered_cut_copper_stairs',
		'minecraft:sandstone',
		'minecraft:waxed_weathered_chiseled_copper',
		'minecraft:infested_stone',
		'minecraft:polished_tuff_slab',
		'minecraft:iron_ore',
		'minecraft:copper_block',
		'minecraft:dead_horn_coral',
		'minecraft:ender_chest',
		'minecraft:packed_mud',
		'minecraft:mossy_stone_brick_slab',
		'minecraft:black_glazed_terracotta',
		'minecraft:blast_furnace',
		'minecraft:waxed_exposed_copper_trapdoor',
		'minecraft:polished_granite',
		'minecraft:cyan_terracotta',
		'minecraft:light_blue_glazed_terracotta',
		'minecraft:cut_copper',
		'minecraft:waxed_cut_copper_slab',
		'minecraft:small_amethyst_bud',
		'minecraft:tuff_stairs',
		'minecraft:dead_bubble_coral_wall_fan',
		'minecraft:cobblestone_stairs',
		'minecraft:dead_fire_coral_fan',
		'minecraft:smooth_sandstone_slab',
		'minecraft:budding_amethyst',
		'minecraft:pink_terracotta',
		'minecraft:netherite_block',
		'minecraft:dead_brain_coral_fan',
		'minecraft:red_nether_brick_stairs',
		'minecraft:mud_brick_slab',
		'minecraft:quartz_bricks',
		'minecraft:stonecutter',
		'minecraft:blue_ice',
		'minecraft:waxed_copper_door',
		'minecraft:copper_door',
		'minecraft:waxed_copper_block',
		'minecraft:dead_horn_coral_wall_fan',
		'minecraft:polished_deepslate_stairs',
		'minecraft:mossy_stone_brick_stairs',
		'minecraft:waxed_exposed_copper_grate',
		'minecraft:mossy_cobblestone_stairs',
		'minecraft:cyan_glazed_terracotta',
		'minecraft:gold_block',
		'minecraft:pink_concrete',
		'minecraft:chiseled_nether_bricks',
		'minecraft:dead_tube_coral_block',
		'minecraft:blue_terracotta',
		'minecraft:ice',
		'minecraft:cut_sandstone',
		'minecraft:light_gray_concrete',
		'minecraft:large_amethyst_bud',
		'minecraft:deepslate_brick_stairs',
		'minecraft:waxed_exposed_copper_bulb',
		'minecraft:dead_tube_coral_wall_fan',
		'minecraft:dead_tube_coral_fan',
		'minecraft:cracked_nether_bricks',
		'minecraft:purple_terracotta',
		'minecraft:waxed_weathered_copper_grate',
		'minecraft:waxed_oxidized_cut_copper',
		'minecraft:polished_diorite_stairs',
		'minecraft:waxed_exposed_chiseled_copper',
		'minecraft:deepslate_coal_ore',
		'minecraft:raw_copper_block',
		'minecraft:exposed_copper_grate',
		'minecraft:deepslate_diamond_ore',
		'minecraft:soul_lantern',
		'minecraft:end_stone',
		'minecraft:polished_deepslate',
		'minecraft:pink_glazed_terracotta',
		'minecraft:crafter',
		'minecraft:tuff',
		'minecraft:blue_concrete',
		'minecraft:smooth_red_sandstone_stairs',
		'minecraft:lodestone',
		'minecraft:orange_terracotta',
		'minecraft:smooth_stone_slab',
		'minecraft:bricks',
		'minecraft:yellow_terracotta',
		'minecraft:dead_fire_coral_wall_fan',
		'minecraft:cut_red_sandstone',
		'minecraft:furnace',
		'minecraft:waxed_exposed_cut_copper_slab',
		'minecraft:exposed_cut_copper',
		'minecraft:chiseled_stone_bricks',
		'minecraft:polished_blackstone_bricks',
		'minecraft:weathered_copper_bulb',
		'minecraft:deepslate_copper_ore',
		'minecraft:blue_glazed_terracotta',
		'minecraft:smooth_red_sandstone_slab',
		'minecraft:exposed_copper_door',
		'minecraft:lightning_rod',
		'minecraft:tuff_wall',
		'minecraft:waxed_copper_bulb',
		'minecraft:waxed_exposed_copper',
		'minecraft:nether_quartz_ore',
		'minecraft:stone_pressure_plate',
		'minecraft:fire_coral_block',
		'minecraft:polished_deepslate_slab',
		'minecraft:hopper',
		'minecraft:waxed_weathered_copper_bulb',
		'minecraft:cobblestone_slab',
		'minecraft:white_glazed_terracotta',
		'minecraft:red_sandstone_stairs',
		'minecraft:iron_block',
		'minecraft:nether_bricks',
		'minecraft:smooth_sandstone_stairs',
		'minecraft:quartz_stairs',
		'minecraft:diorite_stairs',
		'minecraft:piston_head',
		'minecraft:copper_grate',
		'minecraft:oxidized_cut_copper_slab',
		'minecraft:gray_terracotta',
		'minecraft:green_concrete',
		'minecraft:chiseled_copper',
		'minecraft:heavy_weighted_pressure_plate',
		'minecraft:exposed_copper_trapdoor',
		'minecraft:sandstone_stairs',
		'minecraft:deepslate',
		'minecraft:purpur_pillar',
		'minecraft:obsidian',
		'minecraft:red_nether_brick_slab',
		'minecraft:polished_andesite_slab',
		'minecraft:nether_brick_fence',
		'minecraft:blackstone_slab',
		'minecraft:deepslate_iron_ore',
		'minecraft:white_terracotta',
		'minecraft:deepslate_tiles',
		'minecraft:mud_bricks',
		'minecraft:purpur_slab',
		'minecraft:waxed_weathered_copper_door',
		'minecraft:chiseled_red_sandstone',
		'minecraft:polished_basalt',
		'minecraft:red_glazed_terracotta',
		'minecraft:brick_slab',
		'minecraft:respawn_anchor',
		'minecraft:conduit',
		'minecraft:yellow_glazed_terracotta',
		'minecraft:granite_slab',
		'minecraft:smooth_basalt',
		'minecraft:copper_bulb',
		'minecraft:ancient_debris',
		'minecraft:polished_tuff_stairs',
		'minecraft:mossy_cobblestone',
		'minecraft:polished_blackstone_brick_slab',
		'minecraft:dark_prismarine_stairs',
		'minecraft:spawner',
		'minecraft:magma_block',
		'minecraft:exposed_cut_copper_slab',
		'minecraft:cobbled_deepslate_stairs',
		'minecraft:cyan_concrete',
		'minecraft:bubble_coral_block',
		'minecraft:tuff_slab',
		'minecraft:redstone_ore',
		'minecraft:end_stone_bricks',
		'minecraft:stone_brick_slab',
		'minecraft:stone_slab',
		'minecraft:polished_blackstone',
		'minecraft:calcite',
		'minecraft:magenta_glazed_terracotta',
		'minecraft:mossy_cobblestone_slab',
		'minecraft:waxed_cut_copper_stairs',
		'minecraft:bone_block',
		'minecraft:waxed_chiseled_copper',
		'minecraft:waxed_weathered_copper',
		'minecraft:stone_bricks',
		'minecraft:prismarine_slab',
		'minecraft:waxed_exposed_cut_copper_stairs',
		'minecraft:polished_blackstone_stairs',
		'minecraft:iron_door',
		'minecraft:polished_andesite',
		'minecraft:cracked_deepslate_tiles',
		'minecraft:mossy_stone_bricks',
		'minecraft:end_stone_brick_stairs',
		'minecraft:iron_bars',
		'minecraft:coal_ore',
		'minecraft:petrified_oak_slab',
		'minecraft:infested_stone_bricks',
		'minecraft:polished_blackstone_brick_stairs',
		'minecraft:cracked_stone_bricks',
		'minecraft:infested_chiseled_stone_bricks',
		'minecraft:purpur_stairs',
		'minecraft:stone_brick_stairs',
		'minecraft:waxed_oxidized_copper_grate',
		'minecraft:nether_brick_slab',
		'minecraft:lime_glazed_terracotta',
		'minecraft:waxed_oxidized_chiseled_copper',
		'minecraft:prismarine_brick_slab',
		'minecraft:cracked_polished_blackstone_bricks',
		'minecraft:polished_andesite_stairs',
		'minecraft:chiseled_deepslate',
		'minecraft:deepslate_lapis_ore',
		'minecraft:polished_tuff',
		'minecraft:quartz_slab',
		'minecraft:smooth_quartz_slab',
		'minecraft:gray_glazed_terracotta',
		'minecraft:brown_concrete',
		'minecraft:stone',
		'minecraft:magenta_concrete',
		'minecraft:smooth_stone',
		'minecraft:deepslate_redstone_ore',
		'minecraft:oxidized_copper',
		'minecraft:waxed_oxidized_copper',
		'minecraft:deepslate_tile_slab',
		'minecraft:cobbled_deepslate',
		'minecraft:light_gray_glazed_terracotta',
		'minecraft:copper_trapdoor',
		'minecraft:polished_diorite',
		'minecraft:emerald_ore',
		'minecraft:waxed_oxidized_copper_door',
		'minecraft:dark_prismarine',
		'minecraft:nether_gold_ore',
		'minecraft:netherrack',
		'minecraft:quartz_pillar',
		'minecraft:white_concrete',
		'minecraft:waxed_oxidized_copper_bulb',
		'minecraft:polished_diorite_slab',
		'minecraft:dripstone_block',
		'minecraft:amethyst_cluster',
		'minecraft:polished_tuff_wall',
		'minecraft:heavy_core',
		'minecraft:red_sandstone_slab',
		'minecraft:weathered_copper',
		'minecraft:sticky_piston',
		'minecraft:tuff_bricks',
		'minecraft:brick_stairs',
		'minecraft:polished_granite_stairs',
		'minecraft:granite',
		'minecraft:dead_fire_coral',
		'minecraft:dead_fire_coral_block',
		'minecraft:oxidized_copper_bulb',
		'minecraft:sandstone_slab',
		'minecraft:smooth_sandstone',
		'minecraft:oxidized_copper_trapdoor',
		'minecraft:waxed_weathered_cut_copper_stairs',
		'minecraft:packed_ice',
		'minecraft:stone_stairs',
		'minecraft:gold_ore',
		'minecraft:waxed_exposed_cut_copper',
		'minecraft:exposed_copper',
		'minecraft:weathered_copper_grate',
		'minecraft:tuff_brick_wall',
		'minecraft:purple_concrete',
		'minecraft:waxed_copper_grate',
		'minecraft:brown_glazed_terracotta',
		'minecraft:chain',
		'minecraft:andesite_slab',
		'minecraft:oxidized_cut_copper_stairs',
		'minecraft:terracotta',
		'minecraft:cut_copper_slab',
		'minecraft:black_concrete',
		'minecraft:bell',
		'minecraft:grindstone',
		'minecraft:granite_stairs',
		'minecraft:horn_coral_block',
		'minecraft:brain_coral_block',
		'minecraft:red_concrete',
		'minecraft:raw_iron_block',
		'minecraft:dead_brain_coral_wall_fan',
		'minecraft:lantern',
		'minecraft:infested_cracked_stone_bricks',
		'minecraft:weathered_cut_copper_slab',
		'minecraft:iron_trapdoor',
		'minecraft:cobbled_deepslate_slab',
		'minecraft:chiseled_tuff',
		'minecraft:deepslate_tile_stairs',
		'minecraft:blackstone_stairs',
		'minecraft:light_blue_terracotta',
		'minecraft:nether_brick_stairs',
		'minecraft:polished_granite_slab',
		'minecraft:observer',
		'minecraft:lapis_block',
		'minecraft:exposed_chiseled_copper',
		'minecraft:red_terracotta',
		'minecraft:medium_amethyst_bud',
		'minecraft:light_gray_terracotta',
		'minecraft:lime_concrete',
		'minecraft:dead_bubble_coral',
		'minecraft:enchanting_table',
		'minecraft:prismarine_brick_stairs',
		'minecraft:waxed_oxidized_cut_copper_stairs',
		'minecraft:oxidized_copper_door',
		'minecraft:deepslate_emerald_ore',
		'minecraft:cut_red_sandstone_slab',
		'minecraft:exposed_copper_bulb',
		'minecraft:prismarine',
		'minecraft:light_weighted_pressure_plate',
		'minecraft:basalt',
		'minecraft:gray_concrete',
		'minecraft:smooth_quartz',
		'minecraft:mud_brick_stairs',
		'minecraft:dead_brain_coral_block',
		'minecraft:deepslate_brick_slab',
		'minecraft:purple_glazed_terracotta',
		'minecraft:tuff_brick_slab',
		'minecraft:cut_sandstone_slab',
		'minecraft:black_terracotta',
		'minecraft:cut_copper_stairs',
		'minecraft:prismarine_stairs',
		'minecraft:waxed_oxidized_copper_trapdoor',
		'minecraft:waxed_oxidized_cut_copper_slab',
		'minecraft:dead_brain_coral',
		'minecraft:dark_prismarine_slab',
		'minecraft:exposed_cut_copper_stairs',
		'minecraft:amethyst_block',
		'minecraft:end_stone_brick_slab',
		'minecraft:brewing_stand',
		'minecraft:diorite_slab',
		'minecraft:lapis_ore',
		'minecraft:emerald_block',
		'minecraft:green_terracotta',
		'minecraft:coal_block',
		'minecraft:magenta_terracotta',
		'minecraft:weathered_copper_door',
		'minecraft:smooth_red_sandstone',
		'minecraft:copper_ore',
		'minecraft:red_nether_bricks',
		'minecraft:yellow_concrete',
		'minecraft:orange_glazed_terracotta',
		'minecraft:crimson_nylium',
		'minecraft:waxed_weathered_cut_copper',
		'minecraft:waxed_exposed_copper_door',
		'minecraft:dead_tube_coral',
		'minecraft:deepslate_gold_ore',
		'minecraft:smooth_quartz_stairs',
		'minecraft:purpur_block',
		'minecraft:warped_nylium',
		'minecraft:gilded_blackstone',
		'minecraft:deepslate_bricks',
		'minecraft:cracked_deepslate_bricks',
		'minecraft:diorite',
		'minecraft:andesite',
		'minecraft:lime_terracotta',
		'minecraft:dead_bubble_coral_block',
		'minecraft:diamond_ore',
		'minecraft:redstone_block',
		'minecraft:red_sandstone',
		'minecraft:diamond_block',
		'minecraft:chiseled_tuff_bricks',
		'minecraft:prismarine_bricks',
		'minecraft:oxidized_cut_copper',
		'minecraft:blackstone',
		'minecraft:dead_bubble_coral_fan',
		'minecraft:orange_concrete',
		'minecraft:crying_obsidian',
		'minecraft:piston',
		'minecraft:dead_horn_coral_fan',
		'minecraft:cobblestone',
		'minecraft:weathered_cut_copper',
		'minecraft:infested_deepslate',
		'minecraft:waxed_weathered_cut_copper_slab',
		'minecraft:oxidized_chiseled_copper',
		'minecraft:dead_horn_coral_block',
		'minecraft:polished_blackstone_slab',
		'minecraft:waxed_copper_trapdoor',
		'minecraft:weathered_chiseled_copper',
		'minecraft:weathered_copper_trapdoor',
		'minecraft:tuff_brick_stairs',
		'minecraft:tube_coral_block',
		'minecraft:andesite_stairs',
		'minecraft:pointed_dripstone',
	strict=False))