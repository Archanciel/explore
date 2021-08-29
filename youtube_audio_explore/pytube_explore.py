import pytube, os, re
from pytube import Playlist

if os.name == 'posix':
	AUDIO_DIR = '/storage/emulated/0/Download/Audiobooks/pytube_explore/'
else:
	AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\pytube_explore\\'

singlevideoUrl = 'https://youtu.be/Eqy6M6qLWGw'
singlevideoUrl ='https://youtu.be/vU1NEZ9sTOM'
#singlevideoUrl = 'https://youtu.be/LhH9uX3kgTI'
#singlevideoUrl = 'https://youtu.be/llAt4-PDX-o'

youtube = pytube.YouTube(singlevideoUrl)
video = youtube.streams.first()
videoTitle = video.title
print(videoTitle)
t=youtube.streams.filter(only_audio=True)
t[0].download(AUDIO_DIR) # not playable by kivy SoundLoader
