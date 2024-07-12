from block_wrangler import *
from pathlib import Path


shaderpack_root = Path(__file__).parent

def main():
	tags = load_tags()

	mapping = BlockMapping.solve({
		'sway': tags['sway'],
		'sway_bottom': tags['sway/lower'] + tags['sway/short'], # Tags can be combined with the +, -, and & operators
		'crops': tags['minecraft:crops'], # Vanilla tags are included
		'water': blocks('minecraft:water'), # Individual blocks can also be referenced by name
		'emissivity': {i:tags[f'lights/{i}'] for i in range(1, 16)} # Use a dictionary to specify a flag with multiple return values (defaults to 0 when absent)
	})

	with shaderpack_root.joinpath('shaders/block.properties').open('w') as f:
		f.write(mapping.render_encoder())
	with shaderpack_root.joinpath('shaders/util/block_properties.glsl').open('w') as f:
		f.write(mapping.render_decoder())
	
	print('Done!')

if __name__ == '__main__':
	main()