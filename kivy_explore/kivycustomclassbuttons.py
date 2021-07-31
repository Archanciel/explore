from kivy.uix.boxlayout import BoxLayout


class KivyCustomClassButtons(BoxLayout):
	def __init__(self, **kwargs):
		super(KivyCustomClassButtons, self).__init__(**kwargs)
	
	# self.ids.next_track.text = 'NEXT TRACK'
	
	def nextTrack(self):
		print('KivyGUI.nextTrack() called')
	
	def previousTrack(self):
		print('KivyGUI.previousTrack() called')
