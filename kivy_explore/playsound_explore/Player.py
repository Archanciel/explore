from kivy.config import Config
Config.set('graphics', 'fullscreen', '0')

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

from os import listdir, path
import os
import sqlite3

class ChooseFile(FloatLayout):
	select = ObjectProperty(None)
	cancel = ObjectProperty(None)

POSITION_SECONDS_CHANGE = 1

if os.name == 'posix':
	AUDIO_DIR = '/storage/9016-4EF8/Audio/Various'
else:
	AUDIO_DIR = 'D:\\Users\\Jean-Pierre\\Downloads\\Audiobooks'

class AudioPlayer(Widget):
	"""
	https://github.com/Ruffus26/AudioPlayer
	"""
	#folder location
	directory = ''
	#current file playing
	nowPlaying = ''
	#List to hold songs
	songs = []
	#List to hold paths
	pathList = []
	#Temporary Song List
	temp_songList = []
	#List of songs paths
	songPath = []
	#Song index
	index = 0

	def open_db(self):
		self.connection = sqlite3.connect('AudioFiles.db')
		self.crs = self.connection.cursor()
		#Create table
		self.crs.execute('CREATE TABLE IF NOT EXISTS SongList(Number INTEGER, Name TEXT, Path TEXT)')

	def update_db(self, data_unit):
		self.crs.execute('INSERT INTO SongList VALUES(? , ? , ?)', data_unit)
		#Save changes to data base
		self.connection.commit()

	def delete_table_db(self):
		self.crs.execute('DELETE FROM SongList')
		self.connection.commit()
		
	def close_db(self):
		self.crs.close()
		self.connection.close()

	def dismiss_popup(self):
		self._popup.dismiss()

	def fileSelect(self):
		content = ChooseFile(select = self.select, cancel = self.dismiss_popup)
		self._popup = Popup(title = 'Select folder', content= content, size_hint = (0.9, 0.9))
		self._popup.open()

	def select(self, path):
		self.directory = path
		self.ids.direct.text = self.directory
		if not self.directory in self.pathList:
			self.pathList.append(self.directory)
			self.getSongs()
			self.dismiss_popup()
		else:
			self.dismiss_popup()
	
	def browse(self):
		#Text entered by user
		self.directory = self.ids.direct.text

		if (self.directory == '') or self.directory in self.pathList:
			self.fileSelect()
		else:
			self.pathList.append(self.directory)
			self.getSongs()

	def getSongs(self):
		self.open_db()
		if not self.directory.endswith('/'):
			self.directory += '/'

		#Check if the directory exists
		if not path.exists(self.directory):
			self.ids.status.text = 'Folder not found'
			self.ids.status.color = (1,0,0,1)
		else:
			self.ids.status.text = ''
			self.ids.scroll.bind(minimum_height = self.ids.scroll.setter('height'))

			#get mp3 files from directory
			for fl in listdir(self.directory):
				if fl.endswith('.mp3'):
					if not fl in self.songs:
						self.temp_songList.append(fl)
						self.songPath.append(self.directory)
						self.index += 1
						tmp_List_item = [self.index, fl, self.directory]
						self.update_db(tmp_List_item)
			
			#If in chosen directory are no mp3 files
			if self.temp_songList == [] and self.directory != '':
				self.ids.status.text = 'No Music Found'
				self.ids.status.color = (1,0,0,1)
			
			self.temp_songList.sort()
			for song in self.temp_songList:
				def playSong(btn):
					try:
						self.nowPlaying.stop()
						self.ids.toggle_play_btn.text = '||'
					except:
						pass
					finally:
						self.currentSong_index = self.songs.index(btn.text + '.mp3')
						self.songFilePathName = self.songPath[self.currentSong_index + 1] + btn.text + '.mp3'
						self.nowPlaying = SoundLoader.load(self.songFilePathName)
						self.nowPlaying.play()
						self.ids.currentPlay.text = btn.text
						self.ids.status.text = ''

				#Song button label
				btn = Button(text = song[:-4], size_hint_x = 1, on_press = playSong)

				#Label song colors
				btn.background_color = (61/255, 61/255, 63/255, 1)

				#Add btn and icon to Scroll Layout
				self.ids.scroll.add_widget(btn)
			self.songs.extend(self.temp_songList)
			self.temp_songList.clear()
			self.close_db()

	def prev_song(self):
		if self.currentSong_index == 0:
			self.currentSong_index = len(self.songs)
		self.nowPlaying.stop()
		self.songFilePathName = self.songPath[self.currentSong_index + 1] + self.songs[self.currentSong_index + 1]
		self.nowPlaying = SoundLoader.load(self.songFilePathName)
		self.nowPlaying.play()
		self.ids.toggle_play_btn.text = '||'
		self.currentSong_index = self.currentSong_index - 1
		self.ids.currentPlay.text = self.songs[self.currentSong_index][:-4]

	def back_to_song_start(self):
		self.nowPlaying.seek(0)
	
	def go_to_song_end(self):
		duration = self.nowPlaying.length
		self.nowPlaying.seek(duration)
	
	def forward_seconds(self):
		"""
		WARNING
		
		seek() and get_pos() only work if ffpyplayer is installed !
		(C:\Program Files\Python39> ./python -m pip install ffpyplayer
		Successfully installed ffpyplayer-4.3.2)
	
		NOT WORKING ON ANDROID SINCE INSTALLING FFPYPLAYER FAILS !

		:return:
		"""
		posSeconds = self.nowPlaying.get_pos()
		duration = self.nowPlaying.length
		
		if posSeconds < duration - POSITION_SECONDS_CHANGE:
			posSeconds += POSITION_SECONDS_CHANGE
			self.nowPlaying.seek(posSeconds)
	
	def backward_seconds(self):
		"""
		WARNING

		seek() and get_pos() only work if ffpyplayer is installed !
		(C:\Program Files\Python39> ./python -m pip install ffpyplayer
		Successfully installed ffpyplayer-4.3.2)
	
		NOT WORKING ON ANDROID SINCE INSTALLING FFPYPLAYER FAILS !

		:return:
		"""
		posSeconds = self.nowPlaying.get_pos()
		
		if posSeconds >= POSITION_SECONDS_CHANGE:
			posSeconds -= POSITION_SECONDS_CHANGE
		else:
			posSeconds = 0
			
		self.nowPlaying.seek(posSeconds)
	
	def toggle_play(self):
		if self.nowPlaying.state == 'stop':
			self.nowPlaying.play()
			self.ids.toggle_play_btn.text = '||'
		else:
			self.nowPlaying.stop()
			self.ids.toggle_play_btn.text = '#'

	def next_song(self):
		if self.currentSong_index == (len(self.songs) - 1):
			self.currentSong_index = -1
		self.nowPlaying.stop()
		self.songFilePathName = self.songPath[self.currentSong_index + 1] + self.songs[self.currentSong_index + 1]
		self.nowPlaying = SoundLoader.load(self.songFilePathName)
		self.nowPlaying.play()
		self.ids.toggle_play_btn.text = '||'
		self.currentSong_index = self.currentSong_index + 1
		self.ids.currentPlay.text = self.songs[self.currentSong_index][:-4]

	def clearInput(self):
		self.songs.clear()
		self.ids.direct.text = ''
		self.ids.scroll.clear_widgets()
		self.pathList.clear()
		self.songPath.clear()

class PlayerApp(App):
	def build(self):
		player = AudioPlayer()
		self.title = 'Audio Player'
		self.icon = 'wicon.png'
		return player


if __name__ == '__main__':
	PlayerApp().run()