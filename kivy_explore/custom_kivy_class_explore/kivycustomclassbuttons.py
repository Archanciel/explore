from kivy.uix.boxlayout import BoxLayout


class KivyCustomClassButtons(BoxLayout):
	def __init__(self, **kwargs):
		super(KivyCustomClassButtons, self).__init__(**kwargs)
	
	def firstButtonPressed(self):
		print('KivyCustomClassButtons.firstButton pressed')
	
	def secondButtonPressed(self):
		print('KivyCustomClassButtons.secondButton pressed')
