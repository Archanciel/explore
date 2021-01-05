import re

def parse(text, pattern):
	listOfParagraphs = []

	for match in re.finditer(pattern, text):
		for subGroup in match.groups():
			listOfParagraphs.append(subGroup)

	return listOfParagraphs
	
def printList(list):
	for line in list:
		print(line, end='')
		
	print()

text = '''
Title

Section one

This is the first section
which contains two lines.


Section two

The section two contains
three lines of information
and is very important
'''  
print(text)
print()

pattern = r'([\w .,:\-\[\]/*<>=\'\(\)]+)(\n\n\n\n|\n\n\n|\n\n|\n|.*)'
 
list = parse(text, pattern)
printList(list)

text = "Hello world 475 times you said that for 2 people"
pattern = r'(\D+)(\d+|.*)'

list = parse(text, pattern)
printList(list)
