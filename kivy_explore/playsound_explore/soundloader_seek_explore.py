from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.lang import Builder

import os

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


class MyLayout(Widget):
	music_file = AUDIO_DIR + "Un résumé audio de ce qu'enseigne ' Le Cours en Miracles '.mp3"
	music_obj = None

	def start_song(self):
		self.music_obj = SoundLoader.load(self.music_file)
		if self.music_obj:
			print(self.music_obj.source)
			print(self.music_obj.length)
			self.ids.song_title.text = self.music_obj.source
			self.ids.slider.max = self.music_obj.length
			self.music_obj.play()

	def change_pos(self, value):
		if self.music_obj is not None:
			self.music_obj.seek(value)


class Awesome(App):
	def build(self):
		self.title = "Hello!"
		return MyLayout()


if __name__ == "__main__":
	Awesome().run()