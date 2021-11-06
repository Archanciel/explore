import ctypes
import time, threading, os
import youtube_dl

PRINT_SECOND_INTERVAL = 1

class YdlDownloadInfoExtractor:
	"""
	The purpose of this class is to print every PRINT_SECOND_INTERVAL second
	the current state info of the video downloaded by youtube_dl.
	"""
	def __init__(self):
		self.lstPrintTime = time.time()
	
	def ydlCallableHook(self, response):
		"""
		Method hooked to youtube_dl.

		:param response:
		"""
		if response['status'] == 'downloading':
			now = time.time()
			if now - self.lstPrintTime >= PRINT_SECOND_INTERVAL:
				print('download bytes {}: {} %. Speed: {}'.format(response["downloaded_bytes"], response["_percent_str"], response["_speed_str"]))
				self.lstPrintTime = now
		elif response['status'] == 'finished':
			print('total download bytes {}. Now, converting to mp3 ...'.format(response["total_bytes"]))

if os.name == 'posix':
	targetAudioDir = '/storage/emulated/0/Download/Audiobooks/test_youtube_dl'
	ydl_opts = {
		'outtmpl': targetAudioDir + '/%(title)s.mp3',
		'format': 'bestaudio/best',
		#'format': 'worstaudio/worst',
		"progress_hooks": [YdlDownloadInfoExtractor().ydlCallableHook],
		'quiet': True
	}
else:
	targetAudioDir = 'C:\\Users\\Jean-Pierre\\Downloads\\Audio\\test\\test_youtube_dl'
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

def youtubeDownloadVideoOnNewThread():
	"""
	Method executed on a separated thread which can be interrupted in order
	to stop youtube_dl download.
	"""
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		meta = ydl.extract_info(videoUrl, download=False)
		videoTitle = meta['title']
		start_time = time.time()
		ydl.download([videoUrl]) # not playable by kivy SoundLoader
		print('{} audio track downloaded. Size: {}, download time: {}'.format(videoTitle,
																			  meta['filesize'],
																			  time.time() - start_time))

class StoppableThread(threading.Thread):
	"""
	Class inheriting from threading.Thread and adding the possibility
	to stop the thread.
	"""
	def __init__(self, **kwarg):
		super().__init__(**kwarg)
		self.daemon = True
	
	def getThreadId(self):
		# returns id of the respective thread
		if hasattr(self, '_thread_id'):
			print('aaa')
			return self._thread_id
		
		for id, thread in threading._active.items():
			if thread is self:
				print('bbb')
				return id
			
	def stop(self):
		threadId = self.getThreadId()
		res = ctypes.pythonapi.PyThreadState_SetAsyncExc(threadId,
														 ctypes.py_object(SystemExit))
		if res > 1:
			ctypes.pythonapi.PyThreadState_SetAsyncExc(threadId, 0)
			print('Exception raise failure')


if __name__ == "__main__":
	t = StoppableThread(target=youtubeDownloadVideoOnNewThread, args=())
	t.start()
	time.sleep(6)
	print('stopping youtube_dl download')
	t.stop()
	t.join()
	print('main program will finish in 2 seconds ...')
	time.sleep(2)
