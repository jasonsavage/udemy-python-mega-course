#!/usr/bin/env python2.7
import re
import os
import json
import fnmatch

DIR = os.path.join('..', 'src', 'assets', 'js')
ENTRY = 'index.js'

# match import from 'filename' and require('filename')
regex = r"from\s'([^']+)'|require\s?\(\s?'([^']+)'"

def get_imports (imports_dict, fname):
	# if fname is already in imports_dict or fname is not a file it doesn't need to be parsed
	if fname not in imports_dict and os.path.isfile(fname):
		print('Checking %s' % fname)
		
		imports_dict[fname] = True
		groups = []
		
		# open file, read contents and run regex to find all JS imports it requires
		with open(fname, 'r') as f: 
			matches = re.finditer(regex, f.read())
			for matchNum, match in enumerate(matches):
				m = match.group(1)
				if m == None:
					m = match.group(2)
				
				if m != None:
					print(' >  %s' % m)
					groups.append(m)
		
		# loop through each JS import and recursively call get_imports 
		for g in groups:
			get_imports(imports_dict, os.path.join(DIR, str(g).replace('/', os.sep) + '.js'))
		
		
def file_in_path (path, filter):
	r = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if fnmatch.fnmatch(name, filter):
				r.append(os.path.join(root, name))
	return r

def main ():
	imports_dict = {}
	unused_imports = []
	
	# starting at entry file, recursively loop through each JS import, and add files to dict
	fname = os.path.join(DIR, ENTRY)
	get_imports(imports_dict, fname)
	
	# loop through each file path in dict, and check if it is in the imports_dict
	codebase = file_in_path(DIR, '*.js')
	for file in codebase:
		# if the file is not in the imports_dict, add it to the unused_imports list
		if file not in imports_dict:
			unused_imports.append(file)
	
	# write output to a text file
	with open('output.json', 'w') as f: 
		f.write(json.dumps(unused_imports, indent=4, separators=(',', ': ')))


main()

