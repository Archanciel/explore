from pathlib import Path
from os.path import isfile, join
from os import listdir
import os

SD_CARD_DIR_TABLET = '/storage/0000-0000'
SD_CARD_DIR_SMARTPHONE = '/storage/9016-4EF8'
SMARTPHONE_INTERNAL_STORAGE = '/storage/emulated/0'


configFilePathName = SD_CARD_DIR_TABLET
configFilePathName = SMARTPHONE_INTERNAL_STORAGE

def getFileOrDirNamesInSpCard(configFilePathName):
	if os.path.isdir(configFilePathName):	
		print(configFilePathName)
	
		return [f for f in listdir(configFilePathName)]


print(getFileOrDirNamesInSpCard(configFilePathName))

