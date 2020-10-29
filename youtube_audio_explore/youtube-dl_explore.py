import os, re
import youtube_dl
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '140'
if os.name == 'posix':
	targetAudioDir = '/storage/emulated/0/Download/Audiobooks'
else:
	targetAudioDir = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\test_audio_downloader_two_files'

playlistUrl = 'https://www.youtube.com/playlist?list=PLzwWSJNcZTMSFWGrRGKOypqN29MlyuQvn'
playlistObject = Playlist(playlistUrl)
playlistObject._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

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

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	for videoUrl in playlistObject.video_urls:
		ydl.download([videoUrl])