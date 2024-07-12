import unittest
from block_wrangler import BlockType, Blocks, BlockMapping

class TestMapping(unittest.TestCase):
	def test_mapping(self):
		a: BlockType = BlockType('test', 'a', {})
		b: BlockType = BlockType('test', 'b', {})
		c: BlockType = BlockType('test', 'c', {})
		d: BlockType = BlockType('test', 'd', {})
		e: BlockType = BlockType('test', 'e', {})
		self.maxDiff = None
		
		mapping = BlockMapping.solve({
			'A': Blocks({a, b, c}),
			'B': Blocks({b, c, d}),
			'C': Blocks({c, d, e})
		}, start_index=1000)
		order_independent_mapping = {entry['flags']:entry['blocks'] for entry in mapping.mapping}
		self.assertDictEqual(order_independent_mapping, {
			frozenset(['A']): Blocks({a}),
			frozenset(['A', 'B']): Blocks({b}),
			frozenset(['A', 'B', 'C']): Blocks({c}),
			frozenset(['B', 'C']): Blocks({d}),
			frozenset(['C']): Blocks({e}),
		})
	
	def test_sequential_mapping_overlap(self):
		a: BlockType = BlockType('test', 'a', {})
		b: BlockType = BlockType('test', 'b', {})
		c: BlockType = BlockType('test', 'c', {})
		d: BlockType = BlockType('test', 'd', {})
		e: BlockType = BlockType('test', 'e', {})

		self.assertRaises(ValueError, lambda:BlockMapping.solve({
			'A': Blocks({a, b, c}),
			'B': Blocks({b, c, d}),
			'C': {i:Blocks({c, d, e}) for i in range(3)}
		}))