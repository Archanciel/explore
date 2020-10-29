import glob, shutil, time, os
from moviepy.editor import *

AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks'
DIR_SEP = '\\'

playListName = 'moviepy_expl'
targetAudioDir = AUDIO_DIR + DIR_SEP + playListName

# deleting files in audio dir
files = glob.glob(targetAudioDir + DIR_SEP + '*')

for f in files:
	os.remove(f)

# restoring mp4 and mp3 file

sourceVideoFileName = 'Magnifique vidéo de Noël.mp4'
sourceAudioFileName = 'exploreAudio.mp3'
sourceVideoFilePathName = targetAudioDir + DIR_SEP + sourceVideoFileName
sourceAudioFilePathName = targetAudioDir + DIR_SEP + sourceAudioFileName
shutil.copy(
	'D:\\Development\\Python\\audiodownload\\test\\testData' + DIR_SEP + sourceVideoFileName,
	sourceVideoFilePathName)
shutil.copy(
	'D:\\Development\\Python\\audiodownload\\test\\testData' + DIR_SEP + sourceAudioFileName,
	sourceAudioFilePathName)

videoclip = VideoFileClip(sourceVideoFilePathName).subclip(0, 5)
audioclip = AudioFileClip(sourceAudioFilePathName)

ts = time.time()

new_audioclip_mixed = CompositeAudioClip([videoclip.audio, audioclip])
new_audioclip_concatenated = concatenate_audioclips([videoclip.audio, audioclip])

# altering the video audio
videoclip.audio = new_audioclip_mixed
videoclip.write_videofile(targetAudioDir + DIR_SEP + "new_video_mixed.mp4")
videoclip.audio = new_audioclip_concatenated
videoclip.write_videofile(targetAudioDir + DIR_SEP + "new_video_concatenated.mp4")

print(time.time() - ts)

# altering the audio only

ts = time.time()

new_audioclip_mixed.fps = 44100
new_audioclip_mixed.write_audiofile(targetAudioDir + DIR_SEP + "new_audio_mixed.mp3")
new_audioclip_concatenated.write_audiofile(targetAudioDir + DIR_SEP + "new_audio_concatenated.mp3")

print(time.time() - ts)
