import re

PATTERN_FULL_PRICE_REQUEST_WITH_OPTIONAL_COMMAND_DATA = r"(\w+)(?: ([\w/:]+)|)(?: ([\w/:]+)|)(?: ([\w/:]+)|)(?: ([\w/:]+)|)(?: (-[a-zA-Z][a-zA-Z]?[\w/:\.]*))?(?: (-[a-zA-Z][a-zA-Z]?[\w/:\.]*))?"

def parseGroups(inputStr):
	'''
	Embedding this trivial code in a method enables to specifically test the correct
	functioning of the used patterns.

	:param inputStr:    string to parse
	:return:
	'''
	pattern = PATTERN_FULL_PRICE_REQUEST_WITH_OPTIONAL_COMMAND_DATA
	match = re.match(pattern, inputStr)
	
	if match != None:
		print(inputStr)
		print(match.groups())

fullRequest_1 = 'eth btc 0 binance -fusd'
fullRequest_2 = 'eth btc 0 binance -f'
fullRequest_3 = 'eth btc 12/11 binance -v -f'
fullRequest_4 = 'eth btc 12/11 23:09 binance -v -f'

parseGroups(fullRequest_1)
parseGroups(fullRequest_2)
parseGroups(fullRequest_3)
parseGroups(fullRequest_4)