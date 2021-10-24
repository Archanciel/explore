from datetime import datetime
import os, re, time
import sys

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
	
if os.name == 'posix':
	targetAudioDir = '/storage/emulated/0/Download/Audiobooks/test_youtube_dl'
	ydl_opts = {
		'outtmpl': targetAudioDir + '/%(title)s.mp3',
		'format': 'bestaudio/best',
		#'format': 'worstaudio/worst',
		'quiet': True
	}
else:
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

#playlistUrl = 'https://www.youtube.com/playlist?list=PLzwWSJNcZTMSFWGrRGKOypqN29MlyuQvn'
playlistUrl = 'https://youtube.com/playlist?list=PLzwWSJNcZTMTA4XDsubBsSfTCVLxqy1jG'
playlistObject = Playlist(playlistUrl)
playlistObject._video_regex = re.compile(r"\"singleVideoUrl\":\"(/watch\?v=[\w-]*)")
singlevideoUrl = 'https://youtu.be/mere5xyUe6A'
downloadPlaylist = False

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	if downloadPlaylist:
		# downloading playlist
		for videoUrl in playlistObject.video_urls:
			meta = ydl.extract_info(videoUrl, download=False)
			videoTitle = meta['title']
			start_time = time.time()
			ydl.download([videoUrl])
			print('{} audio track downloaded. Size: {}, download time: {}'.format(videoTitle, meta['filesize'], time.time() - start_time))
	else:
		# downloading single video
		meta = ydl.extract_info(singlevideoUrl, download=False)
		
		for key in meta:
			if key == 'formats':
				continue
			if key == 'thumbnails':
				continue
			if key == 'automatic_captions':
				continue

			print('{}: {}'.format(key, meta[key]))
			
		videoTitle = meta['title']
		uploadDate = meta['upload_date']
		formatedUploadDate = datetime.strptime(uploadDate, '%Y%m%d').strftime('%Y-%m-%d')
		start_time = time.time()
		ydl.download([singlevideoUrl]) # not playable by kivy SoundLoader
		print('{} {} audio track downloaded. Size: {}, download time: {}'.format(videoTitle, formatedUploadDate, meta['filesize'],
		                                                                      time.time() - start_time))

