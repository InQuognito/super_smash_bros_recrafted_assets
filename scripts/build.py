import json_checks as jsync

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

jsync.length('en_us','es_mx')

src = 'es_mx'
copy_file(src, 'es_ar')
copy_file(src, 'es_cl')
copy_file(src, 'es_ec')
copy_file(src, 'es_es')
copy_file(src, 'es_uy')
copy_file(src, 'es_ve')
