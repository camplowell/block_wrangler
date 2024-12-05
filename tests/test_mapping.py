from typing import Iterable
import unittest
from block_wrangler import BlockType, Blocks, BlockMapping, MappingConfig
from block_wrangler.flags import Flag, IntFlag

class TestMapping(unittest.TestCase):
	def test_mapping(self):
		a: BlockType = BlockType('test', 'a', {})
		b: BlockType = BlockType('test', 'b', {})
		c: BlockType = BlockType('test', 'c', {})
		d: BlockType = BlockType('test', 'd', {})
		e: BlockType = BlockType('test', 'e', {})
		self.maxDiff = None
		
		mapping = BlockMapping.solve({
			'A': Flag(_blocks({a, b, c})),
			'B': Flag(_blocks({b, c, d})),
			'C': Flag(_blocks({c, d, e}))
		}, MappingConfig(start_index=1000))
		order_independent_mapping = {entry['flags']:entry['blocks'] for entry in mapping.mapping}
		self.assertDictEqual(order_independent_mapping, {
			frozenset(['A']): _blocks({a}),
			frozenset(['A', 'B']): _blocks({b}),
			frozenset(['A', 'B', 'C']): _blocks({c}),
			frozenset(['B', 'C']): _blocks({d}),
			frozenset(['C']): _blocks({e}),
		})
	
	def test_sequential_mapping_overlap(self):
		a: BlockType = BlockType('test', 'a', {})
		b: BlockType = BlockType('test', 'b', {})
		c: BlockType = BlockType('test', 'c', {})
		d: BlockType = BlockType('test', 'd', {})
		e: BlockType = BlockType('test', 'e', {})

		self.assertRaises(ValueError, lambda:BlockMapping.solve({
			'A': Flag(_blocks({a, b, c})),
			'B': Flag(_blocks({b, c, d})),
			'C': IntFlag({i:_blocks({c, d, e}) for i in range(3)})
		}))

def _blocks(blocks:Iterable[BlockType]) -> Blocks:
	return Blocks({block:block.state_tuples() for block in blocks})