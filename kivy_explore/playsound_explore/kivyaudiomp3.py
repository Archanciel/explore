from kivy.app import App
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
import youtube_dl

class KivyAudioMp3(App):
	if os.name == 'posix':
		destDir = '/storage/emulated/0/Download/'
	else:
		destDir = 'c:\\temp\\'
		
	videoUrl = 'https://youtu.be/9iPvLx7gotk'
	videoTitle = ''
	
	ydl_opts = {
		'outtmpl': destDir + '%(title)s.%(ext)s',
		'format': 'bestaudio/best',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '128',
		}],
		'quiet': False
	}
	
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		meta = ydl.extract_info(videoUrl, download=False)
		videoTitle = meta['title']
		ydl.download([videoUrl])
		
	sound = SoundLoader.load(destDir + videoTitle + '.mp3')
	
	def build(self):
		return Label(text="KivyAudioMp3 playing")
	
	if sound:
		sound.play()
		
KivyAudioMp3().run()