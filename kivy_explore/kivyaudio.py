import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

class KivyAudio(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def play_sound(self):
		if os.name == 'posix':
			mp3PathFileName = '/storage/emulated/0/Download/Audiobooks/Malika/ess4.mp3'
		else:
			mp3PathFileName = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Malika\\ess7.mp3'
		sound = SoundLoader.load(mp3PathFileName)
		if sound:
			sound.play()

class KivyAudioApp(App):

	def build(self):
		return KivyAudio()

myApp = KivyAudioApp()
myApp.run()
