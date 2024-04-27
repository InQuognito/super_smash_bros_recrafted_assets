from scripts.core import *

from PIL import Image

def resize_image(input_image_path, output_image_path, max_size):
	original_image = Image.open(input_image_path, 'r')
	width, height = original_image.size

	# Calculate the aspect ratio
	aspect_ratio = width / height

	# Determine the new width and height based on the max_size and aspect ratio
	if width > height:
		new_width = max_size
		new_height = int(max_size / aspect_ratio)
	else:
		new_height = max_size
		new_width = int(max_size * aspect_ratio)

	# Resize the image while maintaining the aspect ratio
	resized_image = original_image.resize((new_width, new_height))

	# Save the resized image
	resized_image.save(output_image_path)

max_size = 256  # Maximum bound for the largest dimension

for fighter in ssbrc.fighters:
	for skin in ssbrc.fighters[fighter]['skins']:
		if skin != 'default' and skin != 'gold' and skin != 'shiny':
			input_image_path = f'assets\\ssbrc\\textures\\fighters\\{fighter}\\skins\\{skin}\\render.png'
			output_image_path = f'bin\\renders\\{fighter}_{skin}_render.png'

			resize_image(input_image_path, output_image_path, max_size)
