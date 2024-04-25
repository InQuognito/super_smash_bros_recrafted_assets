import json
from langdetect import detect

path = 'assets\\ssbrc\\lang\\'
ext = '.json'

def length(source, target):
	strict = False
	'''Compares target with source file, returning an error (or warning, depending on the setting) if the file length does not match'''
	# Count
	with open(path + source + ext, 'r', encoding='utf-8') as file:
		f1 = sum(1 for _ in file)
	with open(path + target + ext, 'r', encoding='utf-8') as file:
		f2 = sum(1 for _ in file)

	# Compare
	if f1 != f2:
		print('Build Error: File lengths do not match.')
		if strict:
			exit()
	return 1

def language(file, lang):
	'''Attempts to detect the target language in each string of file, returning a warning if not found'''
	with open(path + file + ext, 'r') as f:
		data = json.load(f)

		i = 0
		for key, value in data.items():
			this_lang = detect(value)
			if this_lang != lang:
				print(f'Translation key \'{key}\' at index {str(i)} is not in the correct language ({lang}).')
			i += 1
	return 1

def validate(source, target):
	'''Run all other checks in file, proceeding on success'''
	length(source, target)
	language(target, 'es')
