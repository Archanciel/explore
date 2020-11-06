import pytube, os

if os.name == 'posix':
	AUDIO_DIR = '/storage/emulated/0/Download/Audiobooks/pytube_explore/'
else:
	AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\pytube_explore\\'

singleVideoUrl = 'https://youtu.be/vU1NEZ9sTOM'

youtube = pytube.YouTube(singleVideoUrl)
video = youtube.streams.first()
videoTitle = video.title
print(videoTitle)
t=youtube.streams.filter(only_audio=True)
t[0].download(AUDIO_DIR + videoTitle)
