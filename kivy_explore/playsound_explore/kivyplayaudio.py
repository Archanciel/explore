import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

class KivyAudio(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def play_sound(self):
		if os.name == 'posix':
			#mp3PathFileName = '/storage/emulated/0/Download/Comment Etudier Un Cours En Miracles .mp3'
			#mp3PathFileName = 'Comment Etudier Un Cours En Miracles .mp3'
			mp3PathFileName = '/storage/9016-4EF8/Audio/Various/Comment Etudier Un Cours En Miracles .mp3'
			oggPathFileName = '/storage/9016-4EF8/Audio/Various/Comment Etudier Un Cours En Miracles.ogg'
			import logging
			logging.info(mp3PathFileName + ': ' + str(os.path.isfile(mp3PathFileName)))
			#files = os.listdir()
			#mp3files = [f for f in files if 'mp3' in f]
			#logging.info(mp3files)
			#logging.info(mp3files[2] + ': ' + str(os.path.isfile(files[2])))
			import tempfile
			from pydub import AudioSegment
			from urllib.request import urlopen

			#data = urlopen('https://sample-videos.com/audio/mp3/crowd-cheering.mp3').read()
			#f = tempfile.NamedTemporaryFile(delete=False)
			#f.write(data)
			AudioSegment.from_mp3(mp3PathFileName).export(oggPathFileName, format='ogg')
			#f.close()
			# unique audio file playable by kivy SoundLoader
			#mp3PathFileName = '/storage/emulated/0/Download/Audiobooks/Malika/ess4.mp3'
			#mp3PathFileName = '/storage/emulated/0/Download/Audiobooks/pytube_explore/Here to help - Give him what he wants.mp4'
			#mp3PathFileName = '/storage/emulated/0/Download/Audiobooks/Various/Dr Blondel, novembre 2020, HFR Fribourg.mp3'
		else:
			mp3PathFileName = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Malika\\ess7.mp3'
			#mp3PathFileName = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Various\\Dr Blondel, novembre 2020, HFR Fribourg.mp3'
		sound = SoundLoader.load(oggPathFileName)
		if sound:
			sound.play()

class KivyPlayAudioApp(App):

	def build(self):
		return KivyAudio()

myApp = KivyPlayAudioApp()
myApp.run()
