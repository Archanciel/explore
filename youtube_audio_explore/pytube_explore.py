import pytube, os

if os.name == 'posix':
	AUDIO_DIR = '/storage/emulated/0/Download/Audiobooks/pytube_explore/'
else:
	AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\pytube_explore\\'

singlevideoUrl = 'https://youtu.be/Eqy6M6qLWGw'

youtube = pytube.YouTube(singlevideoUrl)
video = youtube.streams.first()
videoTitle = video.title
print(videoTitle)
t=youtube.streams.filter(only_audio=True)
t[0].download(AUDIO_DIR) # not playable by kivy SoundLoader
