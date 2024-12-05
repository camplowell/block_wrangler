# Block Wrangler
A Python library to help Minecraft shader developers deal with block IDs.

It allows shader developers to define "flags" that block states can have, and the script will generate both a block.properties file and corresponding GLSL functions to allow those flags to be used directly in shaders.

It includes all Vanilla blocks and tags, as well as a few custom categories that are commonly used in shaders, and automatically enforces that numerical block IDs are both complete and mutually exclusive.

## Installation

```bash
pip install block-wrangler
```

## Usage

Below is a simple example of how to use the library. More complete documentation is coming soon.

```python
from block_wrangler import *
from pathlib import Path


shaderpack_root = Path(__file__).parent

def main():
	tags = load_tags()

	mapping = BlockMapping.solve({
		'sway': EnumFlag({
			'upper': tags['sway/upper'],
			'lower': tags['sway/lower'],
			'hanging': tags['sway/hanging'],
			'floating': tags['sway/floating'],
			'full': tags['sway/full']
		}),
		'sway_slow': Flag(tags['sway/slow']),
		'crops': Flag(tags['minecraft:crops']), # Vanilla tags are included
		'water': Flag(blocks('minecraft:water')) # Individual blocks can also be referenced by name
	})

	with shaderpack_root.joinpath('shaders/block.properties').open('w') as f:
		f.write(mapping.render_encoder())
	with shaderpack_root.joinpath('shaders/util/block_properties.glsl').open('w') as f:
		f.write(mapping.render_decoder())
	
	print('Done!')

if __name__ == '__main__':
	main()
```

## Core Concepts
The block_wrangler library uses a few main concepts:

### Block Types
These represent the different types of blocks that can be found in Minecraft, and all of their properties.

### Tags
Tags generate a semantically meaningful group of block states that can be used to define flags.  
The library comes with all Vanilla tags, and a few more that are commonly used in shaders.

They can use other tags in their definitions, and their actual contents are calculated on demand.

### Block Collections
These are a more concrete representation of a group of block states.
Tags can create them, or you can define them manually.

### Mappings
Mappings store the actual numeric IDs that go into your block.properties file.