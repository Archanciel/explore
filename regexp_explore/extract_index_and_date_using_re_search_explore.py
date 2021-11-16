# https://www.geeksforgeeks.org/python-regex/

import re

INDEX_PATTERN = r'(^[\d-]*)(.*).mp3'
DATE_PATTERN = r'(.*) ([\d-]*).mp3'

fileNameLst = ['97-Funny suspicious looking dog 2013-11-05.mp3',
			   'Funny suspicious looking dog 2013-11-05.mp3',
			   '97-Funny suspicious looking dog.mp3',
			   'Funny suspicious looking dog.mp3']

for fileName in fileNameLst:
	print(fileName)
	
	match = re.search(INDEX_PATTERN, fileName)
	if match.group(1) != '':
		print('index set')
	else:
		print('no index')
		
	match = re.search(DATE_PATTERN, fileName)
	if match is None:
		print('no date')
	else:
		print('date set')
		
	print()
		