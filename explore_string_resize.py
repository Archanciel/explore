x = "A very long string which needs to be splitted into several lines"
chunks, chunk_size = len(x), 54
splittedStr = [ x[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
print(splittedStr)

class StrSplitter:
	@staticmethod
	def splitLineToLines(longLine, maxLineLen, replaceUnderscoreBySpace=False):
		'''
		Splits the oneLineNote string into lines not exceeding maxLineLen and
		returns the lines into a list.

		:param longLine:
		:param maxLineLen:
		:param replaceUnderscoreBySpace
		:return:
		'''
		if longLine == '':
			return []
		
		if replaceUnderscoreBySpace:
			longLine = longLine.replace('_', ' ')
		
		noteWordList = longLine.split(' ')
		noteLine = noteWordList[0]
		noteLineLen = len(noteLine)
		noteLineList = []
		
		for word in noteWordList[1:]:
			wordLen = len(word)
			
			if noteLineLen + wordLen + 1 > maxLineLen:
				noteLineList.append(noteLine)
				noteLine = word
				noteLineLen = wordLen
			else:
				noteLine += ' ' + word
				noteLineLen += wordLen + 1
		
		noteLineList.append(noteLine)
		
		return noteLineList

spl = StrSplitter()
print(spl.splitLineToLines(x, 54))
playlistTitle = 'Test_title_multiple_time_frame_suppress_extract (s01:05:52-01:07:23 e01:15:52-01:17:23 S01:25:52-01:27:23 E01:35:52-01:37:23)'
print(spl.splitLineToLines(playlistTitle, 54))
print(spl.splitLineToLines(playlistTitle, 24, True))
