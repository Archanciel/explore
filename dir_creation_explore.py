import os
from os.path import sep

# https://smallbusiness.chron.com/make-folders-subfolders-python-38545.html

dirsToCreate = 'd:' + sep + 'temp' + sep + 'newdir' + sep + 'newsubdir'
dirsToCreateWithAdditionalSubDir = dirsToCreate + sep + 'additional sub dir'

if not os.path.isdir(dirsToCreateWithAdditionalSubDir):
	os.makedirs(dirsToCreate)
	print(dirsToCreate, 'created')
	os.makedirs(dirsToCreateWithAdditionalSubDir)
	print(dirsToCreateWithAdditionalSubDir, 'created')
else:
	# dirs are removed by os.removedirs() only if they are empty !
	os.removedirs(dirsToCreateWithAdditionalSubDir)
	print(dirsToCreateWithAdditionalSubDir, 'removed')


