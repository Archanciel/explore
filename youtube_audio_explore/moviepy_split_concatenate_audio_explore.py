import glob, shutil, time, os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *

AUDIO_DIR = 'C:\\Users\\Jean-Pierre\\Downloads\\Audio\\test'
DIR_SEP = '\\'

exploreDir = 'moviepy_expl'
targetAudioDir = AUDIO_DIR + DIR_SEP + exploreDir

exploreSaveDir = 'moviepy_expl_save'

# deleting audio files in target audio dir

files = glob.glob(targetAudioDir + DIR_SEP + '*.mp3')

for f in files:
	os.remove(f)


# restoring mp3 file

sourceAudio = 'Here to help Give him what he wants.mp3'

shutil.copy(
	AUDIO_DIR + DIR_SEP + exploreSaveDir + DIR_SEP + sourceAudio,
	targetAudioDir)

sourceAudioFilePath = targetAudioDir + DIR_SEP + sourceAudio

ts = time.time()
extractAudioFilePath_too_short_unplayable = targetAudioDir + DIR_SEP + 'extract_source_too_short_unplayable.mp3'
extractAudioFilePath_too_short_ok = targetAudioDir + DIR_SEP + 'extract_source_too_short_ok.mp3'
extractAudioFilePath_1 = targetAudioDir + DIR_SEP + 'extract_source_1.mp3'
extractAudioFilePath_2 = targetAudioDir + DIR_SEP + 'extract_source_2.mp3'

# extracting audio file portions

ffmpeg_extract_subclip(sourceAudioFilePath, 4, 8, targetname=extractAudioFilePath_too_short_unplayable)
ffmpeg_extract_subclip(sourceAudioFilePath, 3, 9, targetname=extractAudioFilePath_1)
ffmpeg_extract_subclip(sourceAudioFilePath, 12, 25, targetname=extractAudioFilePath_2)

# concatenating valid audio file portions

audioclip_1 = AudioFileClip(extractAudioFilePath_1)
audioclip_2 = AudioFileClip(extractAudioFilePath_2)

new_audioclip_concatenated = concatenate_audioclips([audioclip_1, audioclip_2])
new_audioclip_concatenated.write_audiofile(targetAudioDir + DIR_SEP + "new_audio_concat.mp3")

print(time.time() - ts)

# trying another way etraction for too short audio clip

import moviepy.editor as mp  # not working on Android

clip = mp.AudioFileClip(sourceAudioFilePath).subclip(t_start=4,
                                                     t_end=5)

clip.write_audiofile(extractAudioFilePath_too_short_ok)
clip.close()

