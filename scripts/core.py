import os
import shutil

from itertools import chain

import ssbrc_data as ssbrc

qm = '\"'
sep_n = '\": '
sep_s = '\": \"'
suf_s = '\",'
suf_e = '\": {'
suf_l = '\": ['
ent = '},'

def remove_file(file):
	if os.path.exists(file):
		os.remove(file)

def remove_path(path):
	if os.path.exists(path):
		shutil.rmtree(path)

def create_path(path):
	if not os.path.exists(path):
		os.makedirs(path)

def reset_path(path):
	remove_path(path)
	create_path(path)

def tab(n):
	'''Returns n number of tabs.'''
	return ("\t" * n)

def count_skins(fighter):
	'''Returns the skin count of the specified fighter.'''
	n = len(ssbrc.fighters[fighter]['skins']) + 2
	if fighter == 'byleth':
		n *= 2
	return n

def has_forms(fighter):
	'''Returns true if the specified fighter has forms, otherwise return false.'''
	if 'true_forms' in ssbrc.fighters[fighter].keys():
		return True
	return False

def forms_isolated_to(fighter):
	'''Returns true if the specified fighter has forms, otherwise return false.'''
	if 'forms_isolated_to' in ssbrc.fighters[fighter].keys():
		return ssbrc.fighters[fighter]['forms_isolated_to']
	return 'none'

def get_parent(fighter, skin, form=''):
	'''Returns the translation key, fixed for values that have merged entries.'''
	default = f'ssbrc:template/fighter/head'
	result = 'ssbrc:'
	if fighter == 'mario' or fighter == 'luigi' or fighter == 'peach' or fighter == 'bowser' or fighter == 'donkey_kong' or fighter == 'king_k_rool' or fighter == 'rob' or fighter == 'shovel_knight':
		result += 'fighters/'
		if fighter == 'luigi':
			result += 'mario'
		else:
			result += f'{fighter}'
		result += '/skins/parent'
		if fighter == 'rob':
			if skin == 'ancient_minister':
				return default
			else:
				result += f'/{form}'
		return result
	else:
		return default

def get_texture(fighter, skin, form=''):
	'''Returns the translation key, fixed for values that have merged entries.'''
	result = f'ssbrc:fighters/{fighter}/skins/'
	if ((fighter == 'byleth' or fighter == 'cloud') and skin == 'gold') or (fighter == 'greninja' and skin == 'hero_style') or (fighter == 'hero' and skin == 'gold' and form == 'kaclang') or (fighter == 'pokemon_trainer' and skin == 'shiny' and form == 'trainer'):
		result += 'default'
	else:
		result += f'{skin}'
	if has_forms(fighter):
		if fighter == 'rob':
			pass
		else:
			result += f'/{form}'
	return result

def js_write(file, str):
	'''Write to file, JSON format.'''
	file.write(str + '\n')
