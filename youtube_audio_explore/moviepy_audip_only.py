import time, glob, os
import moviepy.editor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks'
DIR_SEP = '\\'

playListName = 'Martine_Vives'
targetAudioDir = AUDIO_DIR + DIR_SEP + playListName
sourceVideo = 'Consultation Annales Akashiques 19 nov 2020.mp4'
sourceVideoFilePath = targetAudioDir + DIR_SEP + sourceVideo

# deleting files in audio dir
files = glob.glob(targetAudioDir + DIR_SEP + '*.mp3')

for f in files:
	os.remove(f)

#video = moviepy.editor.VideoFileClip(sourceVideoFilePath) # not useful !
#audio = video.audio


print('\nmoviepy.editor.AudioFileClip(sourceVideoFilePath, fps=22050)\n')
ts = time.time()
audio = moviepy.editor.AudioFileClip(sourceVideoFilePath, fps=22050)
audioFilePath = targetAudioDir + DIR_SEP + 'Consultation Annales Akashiques 19 nov 2020_4.mp3'
audio.write_audiofile(audioFilePath)
audio.close()
print(time.time() - ts) # 37.5 sec


print('\nffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=64, fps=44100)\n')
ts = time.time()
audioFilePath = targetAudioDir + DIR_SEP + 'Consultation Annales Akashiques 19 nov 2020_5.mp3'

# fps=44100 ---> 34.5 sec
ffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=64, fps=44100)
print(time.time() - ts)


print('\nffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=64, fps=22050)\n')
ts = time.time()
audioFilePath = targetAudioDir + DIR_SEP + 'Consultation Annales Akashiques 19 nov 2020_6.mp3'

# fps=22050 ---> 19.7 sec quality ok !
ffmpeg_extract_audio(sourceVideoFilePath, audioFilePath, bitrate=64, fps=22050)
print(time.time() - ts)