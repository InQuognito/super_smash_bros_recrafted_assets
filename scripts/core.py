import os
import shutil

import ssbrc_data as ssbrc

qm = '\"'
sep_n = '\": '
sep_s = '\": \"'
suf_s = '\",'
suf_e = '\": {'
suf_l = '\": ['
ent = '},'

def remove_path(path):
	if os.path.exists(path):
		shutil.rmtree(path)

def create_path(path):
	if not os.path.exists(path):
		os.makedirs(path)

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
	if 'forms' in ssbrc.fighters[fighter].keys():
		return True
	return False

def get_parent(fighter, skin):
	'''Returns the translation key, fixed for values that have merged entries.'''
	default = f'ssbrc:template/fighter/head'
	if fighter == 'mario' or fighter == 'luigi' or fighter == 'bowser' or fighter == 'donkey_kong' or fighter == 'king_k_rool' or fighter == 'rob' or fighter == 'shovel_knight':
		if fighter == 'bowser' and skin != 'bowsette':
			return 'ssbrc:fighters/bowser/skins/parent'
		elif fighter == 'rob':
			pass
		return f'ssbrc.fighters.skin.{skin}'
	elif skin == 'flower_power' or skin == 'penguin':
		return f'ssbrc.series.super_mario_bros.skin.{skin}'
	elif skin == 'shiny' or skin == 'shadow':
		return f'ssbrc.series.pokemon.skin.{skin}'
	elif skin == 'player_2':
		return f'ssbrc.fighters.skin.player_2'
	else:
		return default

def js_write(file, str):
	'''Write to file, JSON format.'''
	file.write(str + '\n')
