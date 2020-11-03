import pytube, os

url = 'https://youtu.be/vU1NEZ9sTOM'

youtube = pytube.YouTube(url)
video = youtube.streams.first()

if os.name == 'posix':
	AUDIO_DIR = '/storage/emulated/0/Download/Audiobooks'
else:
	AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks'

video.download(AUDIO_DIR)