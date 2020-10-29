class AudioExtractor:
	def suppressFrames(self, suppressFrameList):
		suppressFrameNb = len(suppressFrameList)
		clips = []
		duration = 18
		
		for extractIdx in range(suppressFrameNb + 1):
			if extractIdx == 0:
				endValue = suppressFrameList[0][0]
				
				if endValue == 0:
					# suppress frame is starting at 0 !
					continue
				
				clips.append([0, endValue])
			elif extractIdx == suppressFrameNb:
				clips.append([suppressFrameList[extractIdx - 1][1], duration])
			else:
				clips.append([suppressFrameList[extractIdx - 1][1], suppressFrameList[extractIdx][0]])
		
		print('Time frames kept for suppress frame list{}:'.format(suppressFrameList))
		print(clips)
				
if __name__ == "__main__":
	ae = AudioExtractor()
	suppressFrameList = [[4, 7],
						 [11, 13],
						 [15, 17]]
						 
	ae.suppressFrames(suppressFrameList)

	print()
	
	suppressFrameList = [[0, 8],
	                     [11, 13],
	                     [15, 17]]
	
	ae.suppressFrames(suppressFrameList)
