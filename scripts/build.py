import json_checks as jsync

from core import *

# Config
path = jsync.path
ext = jsync.ext
source = path + 'en_us' + ext
target = path + 'es_mx' + ext

def copy_file(input, output):
	'''Copies input file to output file. Forces file extension conforming.'''
	with open(dir + input + ext, 'r', encoding='utf-8') as in_file:
		contents = in_file.read()
	with open(dir + output + ext, 'w', encoding='utf-8') as out_file:
		out_file.write(contents)

	print('Successfully copied ' + input + ' to ' + output + '.')

remove_file(path + 'es_ar' + ext)
remove_file(path + 'es_cl' + ext)
remove_file(path + 'es_ec' + ext)
remove_file(path + 'es_es' + ext)
remove_file(path + 'es_uy' + ext)
remove_file(path + 'es_ve' + ext)

src = 'es_mx'
if jsync.compare(source, target):
	copy_file(src, 'es_ar')
	copy_file(src, 'es_cl')
	copy_file(src, 'es_ec')
	copy_file(src, 'es_es')
	copy_file(src, 'es_uy')
	copy_file(src, 'es_ve')
