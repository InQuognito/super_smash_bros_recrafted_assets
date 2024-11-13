from core import *

fighters_temp = dict(sorted(ssbrc.fighters.items(), key=lambda x: x[1]['model']))

def skin_model(fighter, skin):
	for form in ssbrc.fighters[fighter]['forms']:
		path = f'assets\\ssbrc\\models\\item\\fighter\\'
		create_path(path)
		with open(f'{path}{fighter}\\{skin}\\{form}.json', 'w') as file:
			js_write(file, '{')
			js_write(file, tab(1) + qm + 'parent' + sep_s + get_parent(fighter, skin, form) + suf_s)
			js_write(file, tab(1) + qm + 'textures' + suf_e)
			js_write(file, tab(2) + qm + 'base' + sep_s + get_texture(fighter, skin, form) + qm)
			js_write(file, tab(1) + '}')
			js_write(file, '}')

def equipment_model(path='assets\\ssbrc\\models\\equipment\\fighter\\'):
	for fighter in ssbrc.fighters:
		reset_path(path + fighter)
		for skin in chain(['default','gold'], ssbrc.fighters[fighter]['skins']):
			create_path(path + fighter + '\\' + skin)
			for form in ssbrc.fighters[fighter]['forms']:
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
					if fighter == 'pit' and form == 'wings':
						js_write(file, tab(2) + '],')
						js_write(file, tab(2) + qm + 'wings' + suf_l)
						js_write(file, tab(3) + '{ "texture": "' + f'ssbrc:fighter/{fighter}/default' + '" }')
						js_write(file, tab(2) + ']')
					else:
						js_write(file, tab(2) + ']')
					js_write(file, tab(1) + '}')
					js_write(file, '}')

def create_skin_model(path='assets\\ssbrc\\models\\item\\fighter\\'):
	create_path(path)
	for fighter in ssbrc.fighters:
		create_path(f'{path}\\{fighter}')
		for skin in chain(['default','gold'], ssbrc.fighters[fighter]['skins']):
			create_path(f'{path}\\{fighter}\\{skin}')
			for form in ssbrc.fighters[fighter]['forms']:
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
