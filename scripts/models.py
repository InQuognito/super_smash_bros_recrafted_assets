from core import *

fighters_temp = dict(sorted(ssbrc.fighters.items(), key=lambda x: x[1]['model']))

def skin_model(fighter, skin):
	if has_forms(fighter):
		for form in ssbrc.fighters[fighter]['forms']:
			if form != 'charizard':
				with open(f'assets\\ssbrc\\models\\fighters\\{fighter}\\skins\\{skin}\\{form}.json', 'w') as file:
					js_write(file, '{')
					js_write(file, tab(1) + qm + 'parent' + sep_s + get_parent(fighter, skin, form) + suf_s)
					js_write(file, tab(1) + qm + 'textures' + suf_e)
					js_write(file, tab(2) + qm + 'base' + sep_s + get_texture(fighter, skin, form) + qm)
					js_write(file, tab(1) + '}')
					js_write(file, '}')
	else:
		with open(f'assets\\ssbrc\\models\\fighters\\{fighter}\\skins\\{skin}.json', 'w') as file:
			js_write(file, '{')
			js_write(file, tab(1) + qm + 'parent' + sep_s + get_parent(fighter, skin) + suf_s)
			js_write(file, tab(1) + qm + 'textures' + suf_e)
			js_write(file, tab(2) + qm + 'base' + sep_s + get_texture(fighter, skin) + qm)
			js_write(file, tab(1) + '}')
			js_write(file, '}')

def create_skin_model():
	for fighter in ssbrc.fighters:
		for skin in ['default','gold']:
			skin_model(fighter, skin)
		for skin in ssbrc.fighters[fighter]['skins']:
			if skin != 'bowsette':
				skin_model(fighter, skin)

def create_head_cmd():
	with open('assets\\minecraft\\models\\item\\barrier.json', 'w') as file:
		js_write(file, '{')
		js_write(file, tab(1) + qm + 'parent' + sep_s + 'minecraft:item/generated' + suf_s)
		js_write(file, tab(1) + qm + 'textures' + suf_e)
		js_write(file, tab(2) + qm + 'layer0' + sep_s + 'minecraft:item/barrier' + qm)
		js_write(file, tab(1) + ent)
		js_write(file, tab(1) + qm + 'overrides' + suf_l)
		for fighter in fighters_temp:
			i = fighters_temp[fighter]['model']
			has_forms = False
			if 'forms' in fighters_temp[fighter].keys():
				has_forms = True
			for skin in ['default','gold']:
				if has_forms == True:
					for form in fighters_temp[fighter]['forms']:
						js_write(file, tab(2) + '{ "predicate": { "custom_model_data": '+ str(i) + ' }, "model": "ssbrc:fighters/' + fighter + '/skins/' + skin + '/' + form + '" },')
						i += 1
				else:
					js_write(file, tab(2) + '{ "predicate": { "custom_model_data": '+ str(i) + ' }, "model": "ssbrc:fighters/' + fighter + '/skins/' + skin + '" },')
					i += 1
			for skin in fighters_temp[fighter]['skins']:
				if 'forms' in fighters_temp[fighter]['skins'][skin].keys():
					if fighters_temp[fighter]['skins'][skin]['forms'] == False:
						has_forms = False
					else:
						has_forms = True
				if has_forms == True:
					for form in fighters_temp[fighter]['forms']:
						js_write(file, tab(2) + '{ "predicate": { "custom_model_data": '+ str(i) + ' }, "model": "ssbrc:fighters/' + fighter + '/skins/' + skin + '/' + form + '" },')
						i += 1
				else:
					js_write(file, tab(2) + '{ "predicate": { "custom_model_data": '+ str(i) + ' }, "model": "ssbrc:fighters/' + fighter + '/skins/' + skin + '" },')
					i += 1
			js_write(file, '')

		js_write(file, tab(2) + '{ "predicate": { "custom_model_data": 9999 }, "model": "ssbrc:fighters/random" },')
		js_write(file, tab(2) + '{ "predicate": { "custom_model_data": 10000 }, "model": "ssbrc:fighters/spectator" },\n')

		js_write(file, tab(2) + '{ "predicate": { "custom_model_data": 99999 }, "model": "ssbrc:items/pokeball" },\n')

		js_write(file, tab(2) + '{ "predicate": { "custom_model_data": 9999991 }, "model": "ssbrc:ui/arrow_left" },')
		js_write(file, tab(2) + '{ "predicate": { "custom_model_data": 9999992 }, "model": "ssbrc:ui/arrow_right" }')

		js_write(file, tab(1) + ']')
		js_write(file, '}')

def create_miiverse_cmd():
	with open('assets\\minecraft\\models\\item\\painting.json', 'w') as file:
		js_write(file, '{')
		js_write(file, tab(1) + qm + 'parent' + sep_s + 'minecraft:item/generated' + suf_s)
		js_write(file, tab(1) + qm + 'textures' + suf_e)
		js_write(file, tab(2) + qm + 'layer0' + sep_s + 'minecraft:item/painting' + qm)
		js_write(file, tab(1) + ent)
		js_write(file, tab(1) + qm + 'overrides' + suf_l)

		fighter_count = len(fighters_temp)
		n = 1
		for fighter in fighters_temp:
			if fighter != 'peach':
				i = fighters_temp[fighter]['model']
				for post in range(0, fighters_temp[fighter]['miiverse_posts']):
					if n == fighter_count and post == (fighters_temp[fighter]['miiverse_posts'] - 1):
						js_write(file, tab(2) + '{ "predicate": { "custom_model_data": '+ str(i) + ' }, "model": "ssbrc:stages/miiverse/posts/' + fighter + '/' + str(post) + '" }')
					else:
						js_write(file, tab(2) + '{ "predicate": { "custom_model_data": '+ str(i) + ' }, "model": "ssbrc:stages/miiverse/posts/' + fighter + '/' + str(post) + '" },')
				i += 1
				n += 1

		js_write(file, tab(1) + ']')
		js_write(file, '}')

#create_skin_model()
#create_head_cmd()

create_miiverse_cmd()
