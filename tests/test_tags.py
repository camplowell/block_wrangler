import unittest

from block_wrangler import TagLibrary, BlockType, BlockState, Tag

class TestTags(unittest.TestCase):
	def test_tag_creation(self):
		tags = TagLibrary()
		tag = tags.touch('example')
		self.assertEqual(id(tag), id(tags.touch('example')))
	
	def test_tag_reinit(self):
		tags = TagLibrary()
		tag = tags.touch('example')
		stone = BlockType('minecraft', 'stone', {})
		tag.add([stone])
		self.assertIn(stone, tags['example'].blocks())

	def test_tag_filter(self):
		tags = TagLibrary()
		tag = tags.touch('example')
		oak_slab = BlockType('minecraft', 'oak_slab', {'type': ('top', 'bottom', 'double')})
		tag.add([oak_slab], lambda state: state.type == 'bottom')
		self.assertIn(BlockState(oak_slab, {'type':'bottom'}), tags['example'])
		self.assertNotIn(BlockState(oak_slab, {'type':'top'}), tags['example'])
	
	def test_tag_dependencies(self):
		tags = TagLibrary()
		a = tags.touch('a')
		b = tags.touch('b')
		stone = BlockType('minecraft', 'stone', {})
		cobblestone = BlockType('minecraft', 'cobblestone', {})
		a.add([cobblestone])
		b.add(a)
		a.add([stone])

		actual = b.resolve()
		self.assertIn(stone, actual)
		self.assertIn(cobblestone, actual)
	
	def test_tag_children(self):
		tags = TagLibrary()
		a = tags.touch('a')
		b = tags.touch('a/b')

		stone = BlockType('minecraft', 'stone', {})
		b.add([stone])
		self.assertIn(stone, a.resolve())
	
	def test_circular_dependencies(self):
		tags = TagLibrary()
		a = tags.touch('a')
		b = tags.touch('b')

		a.add(b)
		self.assertRaises(RecursionError, lambda: b.add(a))

	def test_tag_narrowing(self):
		tags = TagLibrary()
		a = tags.touch('a')
		b = tags.touch('a/b')
		
		a.set_mode(Tag.NarrowedMode(strict=False))
		oak_slab = BlockType('minecraft', 'oak_slab', {'type': ('top', 'bottom', 'double')})
		dirt = BlockType('minecraft', 'dirt', {})
		a.add([oak_slab, dirt])
		
		self.assertIn(BlockState(oak_slab, {'type':'bottom'}), a.resolve())
		
		b.add([oak_slab], filter=lambda state: state.type == 'bottom')

		self.assertIn(BlockState(oak_slab, {'type':'bottom'}), actual := a.resolve())
		self.assertNotIn(BlockState(oak_slab, {'type':'top'}), actual)
		self.assertIn(BlockState(dirt, {}), actual)

		a.set_mode(Tag.NarrowedMode(strict=True))
		self.assertNotIn(BlockState(dirt, {}), a.resolve())
	
	def test_tag_widening(self):
		tags = TagLibrary()
		a = tags.touch('a')
		b = tags.touch('a/b')
		c = tags.touch('a/c')

		b.set_mode(Tag.WidenedMode(lambda state: state.type == 'bottom'))

		oak_slab = BlockType('minecraft', 'oak_slab', {'type': ('top', 'bottom', 'double')})
		cobblestone_slab = BlockType('minecraft', 'cobblestone_slab', {'type': ('top', 'bottom', 'double')})
		dirt = BlockType('minecraft', 'dirt', {})
		a.add([oak_slab, dirt])
		c.add([cobblestone_slab])

		self.assertIn(BlockState(oak_slab, {'type':'bottom'}), b.resolve())
		self.assertIn(BlockState(cobblestone_slab, {'type': 'bottom'}), b.resolve())
		self.assertNotIn(BlockState(oak_slab, {'type':'top'}), b.resolve())
		self.assertNotIn(BlockState(dirt, {}), b.resolve())
