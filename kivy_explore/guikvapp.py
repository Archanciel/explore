from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class KivyGUI(BoxLayout):
	def __init__(self, **kwargs):
		super(KivyGUI, self).__init__(**kwargs)
		self.ids.next_track.text = 'NEXT TRACK'
		
	def nextTrack(self):
		print('KivyGUI.nextTrack() called')
	
	def previousTrack(self):
		print('KivyGUI.previousTrack() called')


class GuiKvApp(App):
	def build(self):
		return KivyGUI()
	
GuiKvApp().run()
