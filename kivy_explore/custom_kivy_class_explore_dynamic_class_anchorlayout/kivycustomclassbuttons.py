from kivy.uix.anchorlayout import AnchorLayout


class KivyCustomClassButtons(AnchorLayout):
	def __init__(self, **kwargs):
		super(KivyCustomClassButtons, self).__init__(**kwargs)
	
	def firstButtonPressed(self):
		print('KivyCustomClassButtons.firstButton pressed')
		self.parent.firstButtonPressed()
	
	def secondButtonPressed(self):
		print('KivyCustomClassButtons.secondButton pressed')
		self.parent.secondButtonPressed()
