import functools, re

def twoArgsSortFunc(tuple1, tuple2):
	if tuple1[1] > tuple2[1]:
		return 1
	elif tuple2[1] > tuple1[1]:
		return -1
	elif tuple1[0] < tuple2[0]:
		return 1
	elif tuple2[0] < tuple1[0]:
		return -1
	else:
		return 0
		
def oneArgSortFunc(tuple):
	return tuple[1] + ord(tuple[0])

l = [('a', 5), ('b', 3), ('c', 5), ('b', 2), ('b', 3)]
print('default sort: ', sorted(l))
print()
print('oneArgSortFunc: ', sorted(l, key=oneArgSortFunc))
print()
print('twoArgsSortFunc: ', sorted(l, key=functools.cmp_to_key(twoArgsSortFunc)))

filePatternDirDic = {'test*.py': '/test', '*.py': '/', '*.mp3': '/notexist', '*.rd': '/', '*.docx': '/doc', '*.jpg': '/images', '*Rimsky-Korsakov*.mp3': '/mp3/Rimsky Korsakov'}
filePatternDirTupleLst = [item for item in filePatternDirDic.items()]

#with open('temp.txt', 'w') as f:
#	f.write(str(filePatternDirTupleLst))
#f.close()

def convertWildcardExpToRegexpStr(wildcardExp):
	patternStr = wildcardExp.replace("\\", "\\\\")
	patternStr = patternStr.replace(".", "\.")
	patternStr = patternStr.replace("*", ".*")
	patternStr += "\Z"
	
	# no effect !
	# patternStr = "\A" + patternStr
	
	return patternStr

def computeMoveOrder(typeTupleOne, typeTupleTwo):
	wildchardOne, dirOne = typeTupleOne
	wildchardTwo, dirTwo = typeTupleTwo
	
	regexpOne = convertWildcardExpToRegexpStr(wildchardOne)
	patternOne = re.compile(regexpOne)
	
	if dirOne in dirTwo and patternOne.match(wildchardTwo.replace("*", "a")):
		return 1
	else:
		return -1

#filePatternDirTupleLst = [('*.py', '/'), ('test*.py', '/test'), ('*.rd', '/'), ('*.docx', '/doc'), ('*.jpg', '/images')]
print(filePatternDirTupleLst)
print('Using computeMoveOrder() func')
print(sorted(filePatternDirTupleLst, key=functools.cmp_to_key(computeMoveOrder)))
print('Using lambda tuple 1')
print(sorted(filePatternDirTupleLst, key=lambda tup: tup[1], reverse=True))
print('Using lambda tuple 1 split')
print(sorted(filePatternDirTupleLst, key=lambda tup: len(tup[1].split('/')), reverse=True))
