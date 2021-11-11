from os.path import sep
import os

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


class SM(ScreenManager):
	pass


class Screen1(Screen):
	def __init__(self, **kw):
		super().__init__(**kw)
		
		self.rootPath = ''
		
	def setPath(self, path):
		self.rootPath = sep.join(path.split(sep)[:-1]) + sep
		self.ids.select_file.path = path
		
	def selected(self, fileNameLst):
		# displaying selected file path name as a label

		fileNameLines = ''
		
		for filePathName in fileNameLst:
			fileNameLines += filePathName.replace(self.rootPath, '') + '\n'

		self.ids.lb.text = fileNameLines

	def deselect_action(self):
		# access screen1
		s1 = self.manager.get_screen('first')
		# resetting file selection
		s1.ids.select_file.selection = []


# kivy file
kv = Builder.load_string("""
SM:
    Screen1:

<Screen1>:
    name: 'first'

    BoxLayout:
        orientation: 'vertical'

        FileChooserIconView:
            id: select_file
			filters: ["!*.sys", "*.mp3"]    # this avoid pywintypes.error: (32, 'GetFileAttributesEx'
											# exception when clicking on c: list item
            multiselect: True
            on_selection: root.selected(select_file.selection)
        Label:
            id: lb
            text: 'default'
		Button:
			text: 'Deselect all'
			on_press:
				root.deselect_action()
""")


class filechoosing(App):
	def build(self):
		# avoiding red dot put on Kivy screen after mouse right-click
		from kivy import Config
		Config.set('input', 'mouse', 'mouse,disable_multitouch')

		if os.name == 'posix':
			audioDir = '/storage/emulated/0/Download/Audiobooks/various'
		else:
			audioDir = 'C:\\Users\\Jean-Pierre\\Downloads\\Audio'

		kv.current_screen.setPath(audioDir)
		
		return kv


filechoosing().run()