from os.path import sep

MAX_LENGTH = 10
MAX_LENGTH = 15
MAX_LENGTH = 10

SEPARATORS = [sep, ' ', ',', '.', ':', '-', '_']

if sep == '\\':
	# on Windows
	MESSAGE = "c:\\temp\\testing\\audiobooks\\Et l'Univers disparaîtra-t-il: avec mes commentaires"
else:
	# on Android
	MESSAGE = "c:/temp/testing/audiobooks/Et l'Univers disparaîtra: avec mes commentaires"
	
#MESSAGE = "c:/temp/testing/audiobooks/Et l'Univers disparaîtra: avec mes commentaires"
#MESSAGE = "c:/temp/testing/audio books/Et"
#MESSAGE = "c:/temp/testing/myAudiobooks/Et"

def reformatString(sourceStr, maxLength):
	previousSepIndex = 0
	previousSepChar = ''
	currIndex = 0
	currSplitLength = 0
	formattedStr = ''
	previousSplitIndex = 0
	
	for c in sourceStr:
		if c in SEPARATORS:
			previousSepIndex = currIndex
			previousSepChar = c
#			print('previousSepIndex ', previousSepIndex)
		
		currIndex += 1
		currSplitLength += 1
#		print(currSplitLength)
			
		if previousSepChar != ' ':
			if currSplitLength >= maxLength - 1:
				splitEndIndex = previousSepIndex + 1
				splitStr = sourceStr[previousSplitIndex:splitEndIndex]
				
				if splitStr == '':
					continue
					
				formattedStr += splitStr + '\n'
#				print('splitStr', splitStr, ' ', len(splitStr))
				previousSplitIndex = splitEndIndex
				currSplitLength = currIndex - splitEndIndex
		else:
			if currSplitLength > maxLength:
				splitEndIndex = previousSepIndex + 1
				splitStr = sourceStr[previousSplitIndex:splitEndIndex]
				
				if splitStr == '':
					continue
				
				formattedStr += splitStr + '\n'
#				print('splitStr', splitStr, ' ', len(splitStr))
				previousSplitIndex = splitEndIndex
				currSplitLength = currIndex - splitEndIndex - 1

	formattedStr += sourceStr[previousSplitIndex:]
	
	return formattedStr
	
formattedMessage = reformatString(MESSAGE, MAX_LENGTH)
print('MAX_LENGTH ', MAX_LENGTH)
formattedMessageLines = formattedMessage.split('\n')

for line in formattedMessageLines:
	line = line.strip()
	print(line, ' ', len(line))
