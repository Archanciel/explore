from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.lang import Builder

import os, time, threading

SLIDER_UPDATE_FRENQUENCY = 1

if os.name == 'posix':
	AUDIO_DIR = '/storage/emulated/0/Download/Audiobooks/Various/'
else:
	AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks\\Various\\'

Builder.load_string('''
<MyLayout>:
	BoxLayout:
		orientation: "vertical"
		size: root.width, root.height

		Label:
			id: song_title
			text: "Song title!"
			text_size: self.size
			font_size: 32
			valign: "middle"
			halign: "center"

		Slider:
			id: slider
			min: 0
			max: 1
			step: 1
			value: 0
			on_value: root.change_pos(self.value)

		Button:
			text: "Animate!"
			font_size: 32
			on_release: root.start_song()''')


class AsynchSliderUpdater:
	def __init__(self, music_obj, slider):
		self.music_obj = music_obj
		self.slider = slider
	
	def updateSlider(self):
		music_length = self.music_obj.length
		stop = False
		
		while not stop:
			time.sleep(SLIDER_UPDATE_FRENQUENCY)
			music_pos = self.music_obj.get_pos()
			if music_pos < music_length:
				self.slider.value = music_pos
			else:
				stop = True

class MyLayout(Widget):
	"""
	WARNING

	Only work if ffpyplayer is installed !
	(C:\Program Files\Python39> ./python -m pip install ffpyplayer
	Successfully installed ffpyplayer-4.3.2)
	
	NOT WORKING ON ANDROID SINCE INSTALLING FFPYPLAYER FAILS !
	"""
	
	music_file = AUDIO_DIR + "Un résumé audio de ce qu'enseigne ' Le Cours en Miracles '.mp3"
	music_obj = None

	def start_song(self):
		self.music_obj = SoundLoader.load(self.music_file)
		if self.music_obj:
			print(self.music_obj.source)
			print(self.music_obj.length)
			self.ids.song_title.text = self.music_obj.source
			self.ids.slider.max = self.music_obj.length
			
			self.sliderAsynchUpdater = AsynchSliderUpdater(self.music_obj, self.ids.slider)
			t = threading.Thread(target=self.sliderAsynchUpdater.updateSlider, args=())
			t.daemon = True
			t.start()

			self.music_obj.play()

	def change_pos(self, value):
		if self.music_obj is not None:
			if abs(self.music_obj.get_pos() - value) > SLIDER_UPDATE_FRENQUENCY:
				print(value)
				self.music_obj.seek(value)


class Awesome(App):
	def build(self):
		self.title = "Hello!"
		return MyLayout()


if __name__ == "__main__":
	Awesome().run()