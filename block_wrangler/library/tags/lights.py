from typing import Literal
from block_wrangler.tag import TagLibrary
from block_wrangler.block_type import BlockState
from block_wrangler.library.factories import block_types, gather_block_types
from block_wrangler.irange import irange

class Lightable(BlockState):
	lit: Literal['true', 'false']

def load_tags(library:TagLibrary):
	blocks = gather_block_types(signature=Lightable)

	# my intuition is anything with a 'lit' property emits light when it's true (and not when it's false)
	library.touch('lights').add(blocks, lambda state: state.lit == 'true') 
	
	#MARK: light colors
	library.touch('lights/fire') \
		.add(block_types(
			'minecraft:fire',
			'minecraft:torch',
			'minecraft:wall_torch',
			'minecraft:campfire',
			'minecraft:lantern'
		))
	
	library.touch('lights/soulfire') \
		.add(block_types(
			'minecraft:soul_fire',
			'minecraft:soul_torch',
			'minecraft:soul_wall_torch',
			'minecraft:soul_campfire',
			'minecraft:soul_lantern'
		))
	
	library.touch('lights/redstone') \
		.add(block_types(
			'minecraft:redstone_torch',
			'minecraft:redstone_wall_torch',
			'minecraft:redstone_lamp'
		))

	library.touch('lights/15') \
		.add(block_types(
			'minecraft:beacon',
			'minecraft:conduit',
			'minecraft:end_gateway',
			'minecraft:end_portal',
			'minecraft:fire',
			'minecraft:ochre_froglight',
			'minecraft:verdant_froglight',
			'minecraft:pearlescent_froglight',
			'minecraft:glowstone',
			'minecraft:jack_o_lantern',
			'minecraft:lantern',
			'minecraft:lava',
			'minecraft:lava_cauldron',
			'minecraft:campfire',
			'minecraft:sea_lantern',
			'minecraft:shroomlight',
			'minecraft:redstone_lamp',
			'minecraft:copper_bulb'
		))
	
	library.touch('lights/14') \
		.add(block_types(
			'minecraft:end_rod',
			'minecraft:torch',
			'minecraft:wall_torch',
		)) \
		.add(block_types(
			'minecraft:cave_vines',
			'minecraft:cave_vines_plant',
		), lambda state: state.berries == 'true')
	
	library.touch('lights/13') \
		.add(block_types(
			'minecraft:blast_furnace',
			'minecraft:furnace',
			'minecraft:smoker'
		))
	
	library.touch('lights/12') \
		.add(block_types(
			'minecraft:exposed_copper_bulb'
		))
	
	library.touch('lights/11') \
		.add(block_types(
			'minecraft:nether_portal',
		))
	
	library.touch('lights/10') \
		.add(block_types(
			'minecraft:crying_obsidian',
			'minecraft:soul_campfire',
			'minecraft:soul_fire',
			'minecraft:soul_lantern',
			'minecraft:soul_torch',
			'minecraft:soul_wall_torch'
		))
	
	library.touch('lights/9') \
		.add(block_types(
			'minecraft:deepslate_redstone_ore',
			'minecraft:redstone_ore',
		))
	
	library.touch('lights/8') \
		.add(block_types(
			'minecraft:weathered_copper_bulb',
		))
	
	library.touch('lights/7') \
		.add(block_types(
			'minecraft:enchanting_table',
			'minecraft:ender_chest',
			'minecraft:glow_lichen',
			'minecraft:redstone_torch',
			'minecraft:redstone_wall_torch',
		))
	
	library.touch('lights/6') \
		.add(block_types(
			'minecraft:sculk_catalyst',
		))
	
	library.touch('lights/5') \
		.add(block_types(
			'minecraft:amethyst_cluster'
		))
	
	library.touch('lights/4') \
		.add(block_types(
			'minecraft:large_amethyst_bud',
			'minecraft:oxidized_copper_bulb',
		))
	
	library.touch('lights/3') \
		.add(block_types(
			'minecraft:magma_block'
		))
	
	library.touch('lights/2') \
		.add(block_types(
			'minecraft:firefly_bush',
			'minecraft:medium_amethyst_bud'
		))
	
	library.touch('lights/1') \
		.add(block_types(
			'minecraft:brewing_stand',
			'minecraft:brown_mushroom',
			'minecraft:calibrated_sculk_sensor',
			'minecraft:dragon_egg',
			'minecraft:end_portal_frame',
			'minecraft:sculk_sensor',
			'minecraft:small_amethyst_bud'
		))
	
	library.touch('lights/12').add(block_types('minecraft:vault'), lambda state: state.vault_state in ['active', 'ejecting'])
	library.touch('lights/6' ).add(block_types('minecraft:vault'), lambda state: state.vault_state == 'inactive')
	library.touch('lights/8').add(block_types('minecraft:trial_spawner'), lambda state: state.trial_spawner_state not in ['inactive', 'waiting_for_players'])
	library.touch('lights/4').add(block_types('minecraft:trial_spawner'), lambda state: state.trial_spawner_state == 'waiting_for_players')
	
	library.tag_progressive(block_types('minecraft:respawn_anchor'), 'lights', irange(4), 'charges', irange(4, (3, 15)))
	library.tag_progressive(block_types('minecraft:sea_pickle'), 'lights', irange(4), 'pickles', irange(4, (6, 15)), lambda state: state.waterlogged == 'true')
	library.tag_progressive(block_types('minecraft:light'), 'lights', irange(15), 'pickles', irange(15))
