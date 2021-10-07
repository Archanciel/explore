import os
import shutil
from os.path import sep

# https://smallbusiness.chron.com/make-folders-subfolders-python-38545.html

dirsToCreate = 'd:' + sep + 'temp' + sep + 'newdir' + sep + 'newsubdir'
additionalSubDirName = 'additional sub dir'
dirsToCreateWithAdditionalSubDir = dirsToCreate + sep + additionalSubDirName

if not os.path.isdir(dirsToCreateWithAdditionalSubDir):
	os.makedirs(dirsToCreate)
	print(dirsToCreate, 'created')
	os.makedirs(dirsToCreateWithAdditionalSubDir)
	print(dirsToCreateWithAdditionalSubDir, 'with a file created')
	with open(dirsToCreateWithAdditionalSubDir + sep + 'temp.txt', 'w') as f:
		f.write('hello world')
else:
	# dirs are removed by os.removedirs() only if they are empty !
	try:
		os.removedirs(dirsToCreate)
		print(dirsToCreate, 'removed')
	except Exception as e:
		print('Removing ' + dirsToCreate + ' failed {}'.format(e))
		shutil.rmtree(dirsToCreate)
		print('Removing ' + dirsToCreate + ' including {} and the file it contains done with shutil.rmtree({})'.format(additionalSubDirName, dirsToCreate))


