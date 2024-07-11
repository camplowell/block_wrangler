# Block Wrangler
A Python library to help Minecraft shader developers deal with block IDs.

## Installation

### Using pip

```bash
pip install block-wrangler
```

### From source

```bash
git clone git@github.com:camplowell/block_wrangler.git
pip install -e path/to/block_wrangler
```

## Core Concepts
The block_wrangler library uses a few main concepts:

### Block Types
These represent the different types of blocks that can be found in Minecraft, and all of their properties.

### Tags
These represent a method to produce a semantically meaningful group of block states.  
The library comes with all Vanilla tags, and a few more that are commonly used in shaders.

They can use other tags in their definitions, and their actual contents are calculated on demand.

### Block Collections
These are a more concrete representation of a group of block states.
Tags can create them, or you can define them manually.

### Mappings
Mappings store the actual numeric IDs that go into your block.properties file.
They are created by transforming a dictionary whose keys are a semantically meaningful label, and whose values are Block Collections.

## Usage

Below is a simple example of how to use the library. More complete documentation is coming soon.

```python
from block_wrangler import *
from pathlib import Path


shaderpack_root = Path(__file__).parent

def main():
	tags = load_tags()

	mapping = BlockMapping.solve({
		'sway': tags['sway'],
		'sway_bottom': tags['sway/lower'] + tags['sway/short'], # Tags can be combined with the +, -, and & operators
		'crops': tags['minecraft:crops'], # Vanilla tags are included
		'water': blocks('minecraft:water') # Individual blocks can also be referenced by name
	})

	with shaderpack_root.joinpath('shaders/block.properties').open('w') as f:
		f.write(mapping.render_encoder())
	with shaderpack_root.joinpath('shaders/util/block_properties.glsl').open('w') as f:
		f.write(mapping.render_decoder())
	
	print('Done!')

if __name__ == '__main__':
	main()
```