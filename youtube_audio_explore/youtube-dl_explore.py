import os, re
import youtube_dl
from pytube import Playlist

if os.name == 'posix':
	targetAudioDir = '/storage/emulated/0/Download/Audiobooks/test_youtube_dl'
	ydl_opts = {
		'outtmpl': targetAudioDir + '/%(title)s.mp3',
		#	'format': 'bestaudio/best',
		'format': 'worstaudio/worst',
		'quiet': False
	}
else:
	targetAudioDir = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\test_youtube_dl'
	ydl_opts = {
		'outtmpl': targetAudioDir + '\\%(title)s.%(ext)s',
	#	'format': 'bestaudio/best',
		'format': 'worstaudio/worst',
		'postprocessors': [{
							'key': 'FFmpegExtractAudio',
							'preferredcodec': 'mp3',
							'preferredquality': '96',
						}],
	'quiet': False
	}

playlistUrl = 'https://www.youtube.com/playlist?list=PLzwWSJNcZTMSFWGrRGKOypqN29MlyuQvn'
playlistObject = Playlist(playlistUrl)
playlistObject._video_regex = re.compile(r"\"singleVideoUrl\":\"(/watch\?v=[\w-]*)")
singlevideoUrl = 'https://youtu.be/Eqy6M6qLWGw'
downloadPlaylist = False

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	if downloadPlaylist:
		for videoUrl in playlistObject.video_urls:
			meta = ydl.extract_info(videoUrl, download=False)
			videoTitle = meta['title']
			ydl.download([videoUrl])
			print('{} audio track downloaded'.format(videoTitle))
	else:
		# downloading single video
		meta = ydl.extract_info(singlevideoUrl, download=False)
		videoTitle = meta['title']
		ydl.download([singlevideoUrl])
		print('{} audio track downloaded'.format(videoTitle))

