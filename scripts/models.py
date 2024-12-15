from core import *

def skin_model(fighter, skin):
	for form in ssbrc.fighter[fighter]['forms']:
		path = f'assets\\ssbrc\\models\\item\\fighter\\'
		create_path(path)
		with open(f'{path}{fighter}\\{skin}\\{form}.json', 'w') as file:
			js_write(file, '{')
			js_write(file, tab(1) + qm + 'parent' + sep_s + get_parent(fighter, skin, form) + suf_s)
			js_write(file, tab(1) + qm + 'textures' + suf_e)
			js_write(file, tab(2) + qm + 'base' + sep_s + get_texture(fighter, skin, form) + qm)
			js_write(file, tab(1) + '}')
			js_write(file, '}')

def equipment_model(path='assets\\ssbrc\\equipment\\fighter\\'):
	reset_path(path)

	for fighter in ssbrc.fighter:
		create_path(path + fighter)
		for skin in chain(['default','gold'], ssbrc.fighter[fighter]['skin']):
			if has_forms(fighter) and forms_isolated_to(fighter) != 'head':
				for form in ssbrc.fighter[fighter]['forms']:
					create_path(path + fighter + '\\' + skin)
					skin_path = f'{fighter}/{skin}/{form}'
					if fighter == 'pit':
						skin_path = f'{fighter}/{skin}'
						if form == 'wings':
							if skin == 'retro':
								equipment_model_file(f'{path}{skin_path}/{form}', skin_path, f'{fighter}/default')
							else:
								equipment_model_file(f'{path}{skin_path}/{form}', skin_path, skin_path)
						else:
							equipment_model_file(f'{path}{skin_path}/{form}', skin_path)
					elif fighter == 'shovel_knight':
						if form == 'phase_locket':
							skin_path = f'{fighter}/{form}'
							equipment_model_file(f'{path}{fighter}/{skin}/{form}', skin_path)
						else:
							skin_path = f'{fighter}/{skin}'
							equipment_model_file(f'{path}{fighter}/{skin}/{form}', skin_path)
					else:
						equipment_model_file(f'{path}{fighter}/{skin}/{form}', f'{fighter}/{skin}/{form}')
			else:
				if fighter == 'steve' and skin == 'herobrine':
					equipment_model_file(f'{path}{fighter}/{skin}', f'{fighter}/default')
				else:
					equipment_model_file(f'{path}{fighter}/{skin}', f'{fighter}/{skin}')

	skin_path = 'petrified'
	equipment_model_file(f'{path}{skin_path}', skin_path)

def equipment_model_file(path, skin_path, wing_path='null'):
	with open(f'{path}.json', 'w') as file:
		js_write(file, '{')
		js_write(file, tab(1) + qm + 'layers' + suf_e)
		js_write(file, tab(2) + qm + 'humanoid' + suf_l)
		js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{skin_path}' + '" }')
		js_write(file, tab(2) + '],')
		js_write(file, tab(2) + qm + 'humanoid_leggings' + suf_l)
		js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{skin_path}' + '" }')
		if wing_path != 'null':
			js_write(file, tab(2) + '],')
			js_write(file, tab(2) + qm + 'wings' + suf_l)
			js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{wing_path}' + '" }')
		js_write(file, tab(2) + ']')
		js_write(file, tab(1) + '}')
		js_write(file, '}')

def create_skin_model(path='assets\\ssbrc\\models\\item\\fighter\\'):
	create_path(path)
	for fighter in ssbrc.fighter:
		create_path(f'{path}\\{fighter}')
		for skin in chain(['default','gold'], ssbrc.fighter[fighter]['skin']):
			create_path(f'{path}\\{fighter}\\{skin}')
			for form in ssbrc.fighter[fighter]['forms']:
				create_path(path)
				with open(f'{path}{fighter}\\{skin}\\{form}.json', 'w') as file:
					js_write(file, '{')
					js_write(file, tab(1) + qm + 'parent' + sep_s + get_parent(fighter, skin, form) + suf_s)
					js_write(file, tab(1) + qm + 'textures' + suf_e)
					js_write(file, tab(2) + qm + 'base' + sep_s + get_texture(fighter, skin, form) + qm)
					js_write(file, tab(1) + '}')
					js_write(file, '}')

#create_skin_model()

equipment_model()
