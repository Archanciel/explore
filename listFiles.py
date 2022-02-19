import glob
import os
from os.path import sep
import datetime as dt

audioRootDir = '/storage/emulated/0/Music'
audioRootDir = 'C:\\Users\\Jean-Pierre\\Downloads\\Audio'

# list audioRootDir sub-dirs
updtDateSortedSubDirLst = [s for s in os.listdir(audioRootDir) if os.path.isdir(os.path.join(audioRootDir, s))]

# sort audioRootDir sub-dirs by dir update date
updtDateSortedSubDirLst.sort(key=lambda s: os.path.getmtime(os.path.join(audioRootDir, s)), reverse=True)

# building a list of audioRootDir sub-dirs sorted by dir update date, each list
# containing a list of audio Files sorted by file creation date
audioFileHistoryLst = []

for audioSubDir in updtDateSortedSubDirLst:
	audioSubDirLst = [audioSubDir]
	
	# building a list of audio files contained in the audioSubDir
	updtDateSortedAudioFileLst = list(filter(os.path.isfile, glob.glob(audioRootDir + sep + audioSubDir + sep + "*.mp3")))
	
	# sorting the list of audio files by file creation date
	updtDateSortedAudioFileLst.sort(key=lambda x: os.path.getctime(x), reverse=True)
	
	# now building a list of [audio File, audio File creation date] sub lists
	audioSubDirFileNameSubListLst = [[x.split(sep)[-1], dt.datetime.fromtimestamp(os.path.getctime(x)).strftime('%y%m%d')] for x in updtDateSortedAudioFileLst]
	
	audioSubDirLst.append(audioSubDirFileNameSubListLst)
	audioFileHistoryLst.append(audioSubDirLst)

for audioSubDirLst in audioFileHistoryLst:
	print(audioSubDirLst[0])
	for audioFileName in audioSubDirLst[1]:
		print('\t', audioFileName)