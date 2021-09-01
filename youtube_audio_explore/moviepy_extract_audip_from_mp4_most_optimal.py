import time, glob, os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from playsound import playsound

PLAY = False
AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\test'
DIR_SEP = '\\'

testDirName = 'audible_mobizen'
targetAudioDir = AUDIO_DIR + DIR_SEP + testDirName
sourceName = "Audible Et l'Uunivers disparaîtra"
sourceName = "Short low video quality"
sourceVideoFileName = sourceName + ".mp4"
sourceVideoFilePath = targetAudioDir + DIR_SEP + sourceVideoFileName

# deleting audio files in audio dir
files = glob.glob(targetAudioDir + DIR_SEP + '*.mp3')

for f in files:
	os.remove(f)

targetAudioFileName = sourceName + "_ffmpeg_64_22050.mp3"
targetAudioFilePath = targetAudioDir + DIR_SEP + targetAudioFileName
ts = time.time()

# THIS THE OPTIMALEST AUDIO  EXTRACTION
ffmpeg_extract_audio(sourceVideoFilePath, targetAudioFilePath, bitrate=64, fps=22050)
print('\nffmpeg_extract_audio({}, {}, bitrate=64, fps=22050)\n'.format(sourceVideoFilePath, targetAudioFilePath))
audioExtractionTime = str(time.time() - ts)
print(audioExtractionTime) # 37.5 sec
newAudioFilePath = targetAudioFilePath[:-4] + '_' + audioExtractionTime + '.mp3'
os.rename(targetAudioFilePath, newAudioFilePath)

if PLAY:
	playsound(newAudioFilePath)
	input("Type any key to continue ...")
