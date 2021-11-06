from datetime import datetime
import os, re, time

import youtube_dl
from pytube import Playlist

PRINT_SECONDS = 1

class YdlDownloadInfoExtractor:
	def __init__(self):
		self.lstExtractTime = time.time()
	
	def ydlCallableHook(self, response):
		if response['status'] == 'downloading':
			now = time.time()
			if now - self.lstExtractTime >= PRINT_SECONDS:
				print('download bytes {}: {} %. Speed: {}'.format(response["downloaded_bytes"], response["_percent_str"], response["_speed_str"]))
				self.lstExtractTime = now
		elif response['status'] == 'finished':
			print('total download bytes {}. Now, converting to mp3 ...'.format(response["total_bytes"]))

targetAudioDir = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\test\\test_youtube_dl'
ydl_opts = {
	'outtmpl': targetAudioDir + '\\%(title)s.%(ext)s',
	#'format': 'bestaudio/best',
	'format': 'worstaudio/worst',
	'postprocessors': [{
						'key': 'FFmpegExtractAudio',
						'preferredcodec': 'mp3',
						'preferredquality': '96',
					}],
	"progress_hooks": [YdlDownloadInfoExtractor().ydlCallableHook],
	'quiet': True
}

videoUrl = 'https://youtu.be/mere5xyUe6A'

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	meta = ydl.extract_info(videoUrl, download=False)
	videoTitle = meta['title']
	start_time = time.time()
	ydl.download([videoUrl]) # not playable by kivy SoundLoader
	print('{} audio track downloaded. Size: {}, download time: {}'.format(videoTitle,
																			 meta['filesize'],
																			 time.time() - start_time))

