from typing import Literal
from block_wrangler.block_type import BlockState
from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import gather_block_types

class Waterloggable(BlockState):
	waterlogged: Literal['true', 'false']

def load_tags(library:TagLibrary):
	library.touch('waterlogged').add(gather_block_types(signature=Waterloggable), lambda state: state.waterlogged == 'true')