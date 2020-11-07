import os, re
import youtube_dl

if os.name == 'posix':
	targetAudioDir = '/storage/emulated/0/Download/Audiobooks/test_youtube_dl'
	ydl_opts = {
		'outtmpl': targetAudioDir + '/%(title)s.mp3',
		'format': 'bestaudio/best',
		#'format': 'worstaudio/worst',
		'quiet': False
	}
else:
	targetAudioDir = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\test_youtube_dl'
	ydl_opts = {
		'outtmpl': targetAudioDir + '\\%(title)s.%(ext)s',
		#'format': 'bestaudio/best',
		'format': 'worstaudio/worst',
		'postprocessors': [{
							'key': 'FFmpegExtractAudio',
							'preferredcodec': 'mp3',
							'preferredquality': '96',
						}],
	'quiet': False
	}

singlevideoUrl = 'https://youtu.be/Eqy6M6qLWGw'

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	# downloading single video
	meta = ydl.extract_info(singlevideoUrl, download=False)
	videoTitle = meta['title']
	ydl.download([singlevideoUrl]) # not playable by kivy SoundLoader
	print('{} audio track downloaded'.format(videoTitle))

