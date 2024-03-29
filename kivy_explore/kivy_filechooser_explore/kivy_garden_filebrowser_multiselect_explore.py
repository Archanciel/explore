import os

import kivy
import kivy_garden.filebrowser  # I had to use pip install kivy_garden.filebrowser
								# instead of Pycharm package installation !
from kivy import platform
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class FileBrowserApp(App):

	def build(self):
		self.root = FloatLayout()
		button = Button(text='Select Files', pos_hint={'x':0, 'y': 0}, size_hint=(0.2, 0.1))
		button.bind(on_press=self.do_select)
		self.root.add_widget(button)
		return self.root

	def do_select(self, *args):
		homeDir = None
		if platform == 'win':
			homeDir = os.environ["HOMEPATH"]
		elif platform == 'android':
			homeDir = os.path.dirname(os.path.abspath(__file__))
		elif platform == 'linux':
			homeDir = os.environ["HOME"]
		self.fbrowser = kivy_garden.filebrowser.FileBrowser(select_string='Select',
			multiselect=True, filters=['*.mp3'], path=homeDir)
		self.root.add_widget(self.fbrowser)
		self.fbrowser.bind(
			on_success=self._fbrowser_success,
			on_canceled=self._fbrowser_canceled,
			on_submit=self._fbrowser_success)

	def _fbrowser_success(self, fbInstance):
		if len(fbInstance.selection) == 0:
			return
		selected = []
		for file in fbInstance.selection:
			selected.append(os.path.join(fbInstance.path, file))
			print('selected: ' + str(selected))
		self.root.remove_widget(self.fbrowser)
		self.fbrowser = None

	def _fbrowser_canceled(self, instance):
		self.root.remove_widget(self.fbrowser)
		self.fbrowser = None

if __name__=="__main__":
	app = FileBrowserApp()
	app.run()