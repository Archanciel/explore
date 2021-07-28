from kivy.uix.boxlayout import BoxLayout


class KivyCustomClassGUI(BoxLayout):
	def __init__(self, **kwargs):
		super(KivyCustomClassGUI, self).__init__(**kwargs)
	
	# self.ids.next_track.text = 'NEXT TRACK'
	
	def nextTrack(self):
		print('KivyGUI.nextTrack() called')
	
	def previousTrack(self):
		print('KivyGUI.previousTrack() called')
