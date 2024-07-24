import unittest

from block_wrangler import Blocks, filters
from block_wrangler.block_collections import _filter_states
from block_wrangler.block_type import BlockState, BlockType

class TestBlockCollections(unittest.TestCase):
	def test_init_stateless(self):
		oak_planks = BlockType('minecraft', 'oak_planks', {})
		collection = Blocks({oak_planks:{tuple()}})
		self.assertIn(oak_planks, collection)
	
	def test_filter_passthrough(self):
		oak_planks = BlockType('minecraft', 'oak_planks', {})
		oak_slab = BlockType('minecraft', 'oak_slab', {'type': ('top', 'bottom', 'double')})

		collection = Blocks({oak_planks:{tuple()}, oak_slab:{(0,), (1,), (2,)}})
		collection = collection.where(filters.passthrough)

		self.assertIn(BlockState(oak_slab, {'type':'bottom'}), collection)
		self.assertIn(BlockState(oak_slab, {'type':'top'}), collection)
		self.assertIn(oak_planks, collection)
	
	def test_filter_real(self):
		oak_planks = BlockType('minecraft', 'oak_planks', {})
		oak_slab = BlockType('minecraft', 'oak_slab', {'type': ('top', 'bottom', 'double')})

		collection = Blocks({oak_planks:{tuple()}, oak_slab:oak_slab.state_tuples()})
		collection = collection.where(lambda state: state['type'] == 'bottom')

		self.assertIn(BlockState(oak_slab, {'type':'bottom'}), collection)
		self.assertNotIn(BlockState(oak_slab, {'type':'top'}), collection)
		self.assertNotIn(oak_planks, collection)

	def test_union(self):
		oak_planks = BlockType('minecraft', 'oak_planks', {})
		oak_slab = BlockType('minecraft', 'oak_slab', {'type': ('top', 'bottom', 'double')})
		spruce_planks = BlockType('minecraft', 'spruce_planks', {})

		collection_a = Blocks({
			oak_planks:{tuple()}, 
			oak_slab:_filter_states(oak_slab, lambda state: state['type'] in ('bottom', 'double'))
		})
		collection_b = Blocks({
			oak_planks:{tuple()}, 
			spruce_planks:{tuple()},
			oak_slab:_filter_states(oak_slab, lambda state: state['type'] in ('top', 'bottom'))
		})

		expected = Blocks({
			oak_planks:{tuple()}, 
			spruce_planks:{tuple()},
			oak_slab:oak_slab.state_tuples()
		})
		self.assertEqual(collection_a.union(collection_b), expected)
	
	def test_difference(self):
		oak_planks = BlockType('minecraft', 'oak_planks', {})
		oak_slab = BlockType('minecraft', 'oak_slab', {'type': ('top', 'bottom', 'double')})
		spruce_planks = BlockType('minecraft', 'spruce_planks', {})

		collection_a = Blocks({
			oak_planks:{tuple()}, 
			spruce_planks:{tuple()},
			oak_slab:_filter_states(oak_slab, lambda state: state['type'] in ('bottom', 'double'))
		})
		collection_b = Blocks({
			oak_planks:{tuple()}, 
			oak_slab:_filter_states(oak_slab, lambda state: state['type'] in ('top', 'bottom'))
		})

		expected = Blocks({
			spruce_planks:{tuple()},
			oak_slab:_filter_states(oak_slab, lambda state: state['type'] == 'double')
		})
		self.assertEqual(collection_a.difference(collection_b), expected)
	
	def test_intersection(self):
		oak_planks = BlockType('minecraft', 'oak_planks', {})
		oak_slab = BlockType('minecraft', 'oak_slab', {'type': ('top', 'bottom', 'double')})
		spruce_planks = BlockType('minecraft', 'spruce_planks', {})

		collection_a = Blocks({
			oak_planks:{tuple()}, 
			spruce_planks:{tuple()},
			oak_slab:_filter_states(oak_slab, lambda state: state['type'] in ('bottom', 'double'))
		})
		collection_b = Blocks({
			oak_planks:{tuple()}, 
			oak_slab:_filter_states(oak_slab, lambda state: state['type'] in ('top', 'bottom'))
		})

		expected = Blocks({
			oak_planks:{tuple()},
			oak_slab:_filter_states(oak_slab, lambda state: state['type'] == 'bottom')
		})
		self.assertEqual(collection_a.intersection(collection_b), expected)