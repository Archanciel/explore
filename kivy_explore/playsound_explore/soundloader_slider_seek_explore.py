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
<SoundPlayerGUI>:
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
			on_value: root.updateSoundPos(self.value)

		Button:
			text: "Animate!"
			font_size: 32
			on_release: root.startSong()''')


class AsynchSliderUpdater:
	def __init__(self, soundloaderMp3Obj, slider):
		self.soundloaderMp3Obj = soundloaderMp3Obj
		self.mp3PosSliderStop = self.soundloaderMp3Obj.length - SLIDER_UPDATE_FRENQUENCY
		self.slider = slider
	
	def updateSlider(self):
		mp3Pos = self.soundloaderMp3Obj.get_pos()
		
		while mp3Pos < self.mp3PosSliderStop:
			self.slider.value = mp3Pos
			print(mp3Pos)
			time.sleep(SLIDER_UPDATE_FRENQUENCY)
			mp3Pos = self.soundloaderMp3Obj.get_pos()

class SoundPlayerGUI(Widget):
	"""
	WARNING

	Only work if ffpyplayer is installed !
	(C:\Program Files\Python39> ./python -m pip install ffpyplayer
	Successfully installed ffpyplayer-4.3.2)
	
	NOT WORKING ON ANDROID SINCE INSTALLING FFPYPLAYER FAILS !
	"""
	
	music_file = AUDIO_DIR + "Un résumé audio de ce qu'enseigne ' Le Cours en Miracles '.mp3"
	soundloaderMp3Obj = None

	def startSong(self):
		self.soundloaderMp3Obj = SoundLoader.load(self.music_file)
		if self.soundloaderMp3Obj:
			print(self.soundloaderMp3Obj.source)
			print(self.soundloaderMp3Obj.length)
			self.ids.song_title.text = self.soundloaderMp3Obj.source
			self.ids.slider.max = self.soundloaderMp3Obj.length
			self.startSliderUpdateThread()
			self.soundloaderMp3Obj.play()
	
	def startSliderUpdateThread(self):
		sliderAsynchUpdater = AsynchSliderUpdater(self.soundloaderMp3Obj, self.ids.slider)
		t = threading.Thread(target=sliderAsynchUpdater.updateSlider, args=())
		t.daemon = True
		t.start()

	def updateSoundPos(self, value):
		if self.soundloaderMp3Obj is not None:
			if abs(self.soundloaderMp3Obj.get_pos() - value) > SLIDER_UPDATE_FRENQUENCY:
				# test required to avoid mp3 playing perturbation
				print('updateSoundPos', value)
				self.soundloaderMp3Obj.seek(value)
				if self.soundloaderMp3Obj.status == 'stop':
					self.soundloaderMp3Obj.play()
					self.startSliderUpdateThread()


class SoundPlayer(App):
	def build(self):
		self.title = "Hello!"
		return SoundPlayerGUI()


if __name__ == "__main__":
	SoundPlayer().run()