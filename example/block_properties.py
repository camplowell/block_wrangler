from block_wrangler import *

from pathlib import Path
from pprint import pp


shaderpack_root = Path(__file__).parent

def main():
	tags = load_tags()
	print(tags['minecraft:flower'])
	# mapping = BlockMapping.solve({
	# 	'sway': tags['sway'],
	# 	'sway/bottom': tags['sway/lower'] + tags['sway/short'],
	# 	'water': blocks('minecraft:water')
	# })

	# with shaderpack_root.joinpath('shaders/block.properties').open('w') as f:
	# 	f.write(mapping.render_encoder())
	# with shaderpack_root.joinpath('shaders/util/block_properties.glsl').open('w') as f:
	# 	f.write(mapping.render_decoder())
	
	# print('Done!')

if __name__ == '__main__':
	main()