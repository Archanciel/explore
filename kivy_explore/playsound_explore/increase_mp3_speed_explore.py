import os
from pydub import AudioSegment
import soundfile as sf
import pyrubberband as pyrb


def increase_speed(mp3FilePathName, speed):
	sound = AudioSegment.from_file(mp3FilePathName)
	wavFilePathName = mp3FilePathName.split('.')[0] + '.wav'
	sound.export(wavFilePathName, format="wav")
	y, sr = sf.read(wavFilePathName)

	# Play back at 3X speed
	y_stretch = pyrb.time_stretch(y, sr, speed)
	sf.write(wavFilePathName, y_stretch, sr, format='wav')
	
	sound = AudioSegment.from_wav(wavFilePathName)
	
	mp3FilePathNameAccelerated = mp3FilePathName.split('.')[0] + '_speeded' + '.mp3'
	sound.export(mp3FilePathNameAccelerated, format="mp3")
	os.remove(wavFilePathName)
	
	return mp3FilePathNameAccelerated

mp3FilePathName = 'D:\\Users\\Jean-Pierre\\Downloads\\Jancovici.mp3'
mp3FilePathNameAccelerated = increase_speed(mp3FilePathName, 1.25)
# launches the audio file player
os.system(mp3FilePathNameAccelerated)
