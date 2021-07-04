import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

class KivyAudio(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def play_sound(self):
		if os.name == 'posix':
			#mp3PathFileName = '/storage/emulated/0/Download/Audiobooks/test_youtube_dl/Here to help - Give him what he wants.mp3'
			#mp3PathFileName = '/storage/emulated/0/Download/Audiobooks/test_youtube_dl/Wear a mask. Help slow the spread of Covid-19..mp3'
			
			# unique audio file playable by kivy SoundLoader
			mp3PathFileName = '/storage/emulated/0/Download/Audiobooks/Malika/ess4.mp3'
			#mp3PathFileName = '/storage/emulated/0/Download/Audiobooks/pytube_explore/Here to help - Give him what he wants.mp4'
			#mp3PathFileName = '/storage/emulated/0/Download/Audiobooks/Various/Dr Blondel, novembre 2020, HFR Fribourg.mp3'
		else:
			mp3PathFileName = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Malika\\ess7.mp3'
			#mp3PathFileName = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Various\\Dr Blondel, novembre 2020, HFR Fribourg.mp3'
		sound = SoundLoader.load(mp3PathFileName)
		if sound:
			sound.play()

class KivyPlayAudioApp(App):

	def build(self):
		return KivyAudio()

myApp = KivyPlayAudioApp()
myApp.run()
