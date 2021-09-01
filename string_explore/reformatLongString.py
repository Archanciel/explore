#import os.path.SEP
SEP = '/'

MAX_LENGTH = 10
MAX_LENGTH = 15
MAX_LENGTH = 10

SEPARATORS = [SEP, ' ', ',', '.', ':']
MESSAGE = "c:/temp/testing/audiobooks/Et l'Univers disparaîtra: avec mes commentaires"

def reformatString(sourceStr, maxLength):
	previousSepIndex = 0
	currIndex = 0
	currSplitLength = 0
	formattedStr = ''
	previousSplitIndex = 0
	
	for c in sourceStr:
		if c in SEPARATORS:
			previousSepIndex = currIndex
			print('previousSepIndex ', previousSepIndex)
		
		currIndex += 1
		currSplitLength += 1
		print(currSplitLength)
			
		if currSplitLength >= maxLength - 1:
			splitEndIndex = previousSepIndex + 1
			formattedStr += sourceStr[previousSplitIndex:splitEndIndex] + '\n'
			print(formattedStr)
			previousSplitIndex = splitEndIndex
			currSplitLength = 1
			
	formattedStr += sourceStr[previousSplitIndex:]
	
	return formattedStr
	
formattedMessage = reformatString(MESSAGE, MAX_LENGTH)
print(MAX_LENGTH)
print(formattedMessage)