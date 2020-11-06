import os, re
import youtube_dl
from pytube import Playlist

if os.name == 'posix':
	targetAudioDir = '/storage/emulated/0/Download/Audiobooks/test_youtube_dl'
	ydl_opts = {
	'outtmpl': targetAudioDir + '/%(title)s.mp3',
	'format': 'bestaudio/best',
	'quiet': False
	}
else:
	targetAudioDir = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\test_youtube_dl'
	ydl_opts = {
	'outtmpl': targetAudioDir + '\\%(title)s.%(ext)s',
	'format': 'bestaudio/best',
	'postprocessors': [{
						'key': 'FFmpegExtractAudio',
						'preferredcodec': 'mp3',
						'preferredquality': '128',
					}],
	'quiet': False
	}

playlistUrl = 'https://www.youtube.com/playlist?list=PLzwWSJNcZTMSFWGrRGKOypqN29MlyuQvn'
playlistObject = Playlist(playlistUrl)
playlistObject._video_regex = re.compile(r"\"singleVideoUrl\":\"(/watch\?v=[\w-]*)")


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	for videoUrl in playlistObject.video_urls:
		meta = ydl.extract_info(videoUrl, download=False)
		videoTitle = meta['title']
		print('Video title: ' + videoTitle)
		ydl.download([videoUrl])
