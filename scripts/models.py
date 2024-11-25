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

def equipment_model_old(path='assets\\ssbrc\\equipment\\fighter\\'):
	reset_path(path)
	for fighter in ssbrc.fighter:
		for skin in chain(['default','gold'], ssbrc.fighter[fighter]['skin']):
			if has_forms(fighter):
				create_path(path + fighter + '\\' + skin)
				for form in ssbrc.fighter[fighter]['forms']:
					if fighter == 'pit' and form == 'wings':
						wings = True
					else:
						wings = False
					with open(f'{path}{fighter}\\{skin}\\{form}.json', 'w') as file:
						js_write(file, '{')
						js_write(file, tab(1) + qm + 'layers' + suf_e)
						js_write(file, tab(2) + qm + 'humanoid' + suf_l)
						if fighter == 'shovel_knight':
							if form == 'phase_locket':
								js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/{form}' + '" }')
							else:
								js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/{skin}' + '" }')
						else:
							if has_forms(fighter) and forms_isolated_to(fighter) != 'head':
								js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/{skin}/{form}' + '" }')
							else:
								js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/{skin}' + '" }')
						js_write(file, tab(2) + '],')
						js_write(file, tab(2) + qm + 'humanoid_leggings' + suf_l)
						if fighter == 'shovel_knight':
							if form == 'phase_locket':
								js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/{form}' + '" }')
							else:
								js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/{skin}' + '" }')
						else:
							if has_forms(fighter) and forms_isolated_to(fighter) != 'head':
								js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/{skin}/{form}' + '" }')
							else:
								js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/{skin}' + '" }')
						if fighter == 'pit' and skin == 'retro' and form == 'wings':
							js_write(file, tab(2) + '],')
							js_write(file, tab(2) + qm + 'wings' + suf_l)
							js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/default' + '" }')
							js_write(file, tab(2) + ']')
						else:
							js_write(file, tab(2) + ']')
						js_write(file, tab(1) + '}')
						js_write(file, '}')
	equipment_model_file(skin_path='petrified')

def equipment_model(path='assets\\ssbrc\\equipment\\fighter\\'):
	reset_path(path)

	for fighter in ssbrc.fighter:
		for skin in chain(['default','gold'], ssbrc.fighter[fighter]['skin']):
			pass

	equipment_model_file(path, skin_path='petrified')

def equipment_model_file(path, skin_path, wings=False, wing_path=''):
	with open(path + f'{skin_path}.json', 'w') as file:
		js_write(file, '{')
		js_write(file, tab(1) + qm + 'layers' + suf_e)
		js_write(file, tab(2) + qm + 'humanoid' + suf_l)
		js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{skin_path}' + '" }')
		js_write(file, tab(2) + '],')
		js_write(file, tab(2) + qm + 'humanoid_leggings' + suf_l)
		js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{skin_path}' + '" }')
		if wings == True:
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

#equipment_model()
