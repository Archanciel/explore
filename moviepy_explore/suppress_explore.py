import os, shutil

from constants import *

class AudioExtractor:
	def suppressFrames(self, suppressFrameList):
		suppressFrameNb = len(suppressFrameList)
		clips = []
		duration = 18
		
		for extractIdx in range(suppressFrameNb + 1):
			if extractIdx == 0:
				clips.append([0, suppressFrameList[0][0]])
			elif extractIdx == suppressFrameNb:
				clips.append([suppressFrameList[extractIdx - 1][1], duration])
			else:
				clips.append([suppressFrameList[extractIdx - 1][1], suppressFrameList[extractIdx][0]])
		
		print(clips)
				
if __name__ == "__main__":
	ae = AudioExtractor()
	suppressFrameList = [[4, 8],
						 [11, 13],
						 [15, 17]]
						 
	ae.suppressFrames(suppressFrameList)
		