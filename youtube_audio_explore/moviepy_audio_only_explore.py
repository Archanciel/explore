import glob, shutil, time, os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *

AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks'
DIR_SEP = '\\'

playListName = 'moviepy_explore'
targetAudioDir = AUDIO_DIR + DIR_SEP + playListName

# deleting files in audio dir
files = glob.glob(targetAudioDir + DIR_SEP + '*')

for f in files:
	os.remove(f)

# restoring mp3 file

sourceAudio = 'Here to help - Give him what he wants.mp3'
sourceAudioFilePath = targetAudioDir + DIR_SEP + sourceAudio

shutil.copy(
	'D:\\Development\\Python\\audiodownload\\test\\testData' + DIR_SEP + sourceAudio,
	sourceAudioFilePath)

ts = time.time()
extractAudioFilePath_1 = targetAudioDir + DIR_SEP + 'extract_source_1.mp3'
extractAudioFilePath_2 = targetAudioDir + DIR_SEP + 'extract_source_2.mp3'

ffmpeg_extract_subclip(sourceAudioFilePath, 5, 9, targetname=extractAudioFilePath_1)
ffmpeg_extract_subclip(sourceAudioFilePath, 12, 25, targetname=extractAudioFilePath_2)

audioclip_1 = AudioFileClip(extractAudioFilePath_1)
audioclip_2 = AudioFileClip(extractAudioFilePath_2)

new_audioclip_concatenated = concatenate_audioclips([audioclip_1, audioclip_2])
new_audioclip_concatenated.write_audiofile(targetAudioDir + DIR_SEP + "new_audio_concat.mp3")

print(time.time() - ts)
