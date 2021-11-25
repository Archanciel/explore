import time, glob, os
import moviepy.editor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

AUDIO_DIR = 'C:\\Users\\Jean-Pierre\\Downloads\\Audio\\test'
DIR_SEP = '\\'

playListName = 'moviepy_expl'
targetAudioDir = AUDIO_DIR + DIR_SEP + playListName
sourceVideo = 'Here to help Give him what he wants.mp4'
sourceVideoFilePath = targetAudioDir + DIR_SEP + sourceVideo

# deleting audio files in target audio dir

files = glob.glob(targetAudioDir + DIR_SEP + '*.mp3')

for f in files:
	os.remove(f)


print('\nmoviepy.editor.AudioFileClip(sourceVideoFilePath, fps=22050)\n')
ts = time.time()
audio = moviepy.editor.AudioFileClip(sourceVideoFilePath, fps=22050)
audioFilePath = targetAudioDir + DIR_SEP + 'Here to help Give him what he wants.mp3'
audio.write_audiofile(audioFilePath)
audio.close()
print(time.time() - ts) # 37.5 sec


print('\nffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=64, fps=44100)\n')
ts = time.time()
audioFilePath = targetAudioDir + DIR_SEP + 'Here to help Give him what he wants 1.mp3'

# fps=44100 ---> 34.5 sec
ffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=64, fps=44100)
print(time.time() - ts)


print('\nffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=64, fps=22050)\n')
ts = time.time()
audioFilePath = targetAudioDir + DIR_SEP + 'Here to help Give him what he wants 2.mp3'

# fps=22050 ---> 19.7 sec quality ok !
ffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=64, fps=22050)
print(time.time() - ts)


print('\nBEST - ffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=128, fps=22050)\n')
ts = time.time()
audioFilePath = targetAudioDir + DIR_SEP + 'Here to help Give him what he wants 3.mp3'

# fps=22050 ---> 19.7 sec quality ok !
ffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=64, fps=22050)
print(time.time() - ts)