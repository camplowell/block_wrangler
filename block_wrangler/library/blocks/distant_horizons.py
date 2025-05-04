from enum import Flag, auto
from typing import Final

class DHMaterial(Flag):
    DH_NONE = 0
    """The empty flag."""
    DH_BLOCK_UNKNOWN = auto()
    """Any block not in this list that does not emit light"""
    DH_BLOCK_LEAVES = auto()
    """All types of leaves, bamboo, or cactus"""
    DH_BLOCK_STONE = auto()
    """Stone or ore"""
    DH_BLOCK_WOOD = auto()
    """Any wooden item"""
    DH_BLOCK_METAL = auto()
    """Any block that emits a metal or copper sound."""
    DH_BLOCK_DIRT = auto()
    """Dirt, grass, podzol, and coarse dirt."""
    DH_BLOCK_LAVA = auto()
    """Lava."""
    DH_BLOCK_DEEPSLATE = auto()
    """Deepslate, and all it's forms."""
    DH_BLOCK_SNOW = auto()
    """Snow."""
    DH_BLOCK_SAND = auto()
    """Sand and red sand."""
    DH_BLOCK_TERRACOTTA = auto()
    """Terracotta."""
    DH_BLOCK_NETHER_STONE = auto()
    """Blocks that have the "base_stone_nether" tag."""
    DH_BLOCK_WATER = auto()
    """Water..."""
    DH_BLOCK_ILLUMINATED = auto()
    """Any block not in this list that emits light"""

DH_BLOCK_UNKNOWN: Final = DHMaterial.DH_BLOCK_UNKNOWN
"""Any block not in this list that does not emit light"""
DH_BLOCK_LEAVES: Final = DHMaterial.DH_BLOCK_LEAVES
"""All types of leaves, bamboo, or cactus"""
DH_BLOCK_STONE: Final = DHMaterial.DH_BLOCK_STONE
"""Stone or ore"""
DH_BLOCK_WOOD: Final = DHMaterial.DH_BLOCK_WOOD
"""Any wooden item"""
DH_BLOCK_METAL: Final = DHMaterial.DH_BLOCK_METAL
"""Any block that emits a metal or copper sound."""
DH_BLOCK_DIRT: Final = DHMaterial.DH_BLOCK_DIRT
"""Dirt, grass, podzol, and coarse dirt."""
DH_BLOCK_LAVA: Final = DHMaterial.DH_BLOCK_LAVA
"""Lava."""
DH_BLOCK_DEEPSLATE: Final = DHMaterial.DH_BLOCK_DEEPSLATE
"""Deepslate, and all it's forms."""
DH_BLOCK_SNOW: Final = DHMaterial.DH_BLOCK_SNOW
"""Snow."""
DH_BLOCK_SAND: Final = DHMaterial.DH_BLOCK_SAND
"""Sand and red sand."""
DH_BLOCK_TERRACOTTA: Final = DHMaterial.DH_BLOCK_TERRACOTTA
"""Terracotta."""
DH_BLOCK_NETHER_STONE: Final = DHMaterial.DH_BLOCK_NETHER_STONE
"""Blocks that have the "base_stone_nether" tag."""
DH_BLOCK_WATER: Final = DHMaterial.DH_BLOCK_WATER
"""Water..."""
DH_BLOCK_ILLUMINATED: Final = DHMaterial.DH_BLOCK_ILLUMINATED
"""Any block not in this list that emits light"""

DH_NONE: Final = DHMaterial(0)
