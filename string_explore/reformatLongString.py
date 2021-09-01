#import os.path.SEP
SEP = '/'

MAX_LENGTH = 10
MAX_LENGTH = 15
MAX_LENGTH = 20

SEPARATORS = [SEP, ' ', ',', '.', ':']
MESSAGE = "c:/temp/testing/audio books/Et l'Univers disparaîtra: avec mes commentaires"
#MESSAGE = "c:/temp/testing/audio books/Et"
#MESSAGE = "c:/temp/testing/myAudiobooks/Et"

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
			splitStr = sourceStr[previousSplitIndex:splitEndIndex]
			formattedStr += splitStr + '\n'
			print('splitStr', splitStr, ' ', len(splitStr))
			previousSplitIndex = splitEndIndex
			currSplitLength = 1
			
	formattedStr += sourceStr[previousSplitIndex:]
	
	return formattedStr
	
formattedMessage = reformatString(MESSAGE, MAX_LENGTH)
print('MAX_LENGTH ', MAX_LENGTH)
print(formattedMessage)