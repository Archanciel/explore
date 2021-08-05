from kivy.uix.boxlayout import BoxLayout


class KivyCustomClassButtons(BoxLayout):
	def __init__(self, **kwargs):
		super(KivyCustomClassButtons, self).__init__(**kwargs)
	
	def firstButtonPressed(self):
		"""
		Method called by KivyCustomClassSpinner, sub class of
		KivyCustomClassButtons.
		"""
		print('KivyCustomClassButtons.firstButton pressed')
	
	def secondButtonPressed(self):
		"""
		Method called by KivyCustomClassSpinner, sub class of
		KivyCustomClassButtons.
		"""
		print('KivyCustomClassButtons.secondButton pressed')
