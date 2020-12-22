from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class AppGUI(BoxLayout): 
	def __init__(self, **kwargs):
		super(AppGUI, self).__init__(**kwargs)

	def on_pause(self):
		# Here you can save data if needed
		return True

	def on_resume(self):
		# Here you can check if any data needs replacing (usually nothing)
		pass

class BoxlayoutPositionApp(App):
	def build(self):
		return AppGUI()
	
BoxlayoutPositionApp().run()