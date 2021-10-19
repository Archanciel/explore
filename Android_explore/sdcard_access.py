from pathlib import Path
from os.path import isfile, join
from os import listdir
import os

SD_CARD_DIR_TABLET = '/storage/0000-0000'
SD_CARD_DIR_SMARTPHONE = '/storage/9016-4EF8'


configFilePathName = SD_CARD_DIR_TABLET

def getFileOrDirNamesInSpCard():
	if os.path.isdir(SD_CARD_DIR_TABLET):
		sdCardRoot = SD_CARD_DIR_TABLET
	elif os.path.isdir(SD_CARD_DIR_SMARTPHONE):
		sdCardRoot = SD_CARD_DIR_SMARTPHONE
	
	print(sdCardRoot)
	
	return [f for f in listdir(sdCardRoot)]


print(getFileOrDirNamesInSpCard())

