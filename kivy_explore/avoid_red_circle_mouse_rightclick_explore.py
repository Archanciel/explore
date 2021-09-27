from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout


class AppGUI(GridLayout): 
	def __init__(self, **kwargs):
		super(AppGUI, self).__init__(**kwargs)

	def on_pause(self):
		# Here you can save data if needed
		return True

	def on_resume(self):
		# Here you can check if any data needs replacing (usually nothing)
		pass

class AvoidRecCircleMouseRightClickExploreApp(App):
	def build(self):
		# avoiding red dot put on Kivy screen after mouse right-click
		Config.set('input', 'mouse', 'mouse,disable_multitouch')

		return AppGUI()
	
AvoidRecCircleMouseRightClickExploreApp().run()