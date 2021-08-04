from kivy.uix.boxlayout import BoxLayout


class KivyCustomClassButtons(BoxLayout):
	def __init__(self, **kwargs):
		super(KivyCustomClassButtons, self).__init__(**kwargs)
	
	def firstButtonPressed(self):
		print('KivyCustomClassButtons.firstButton pressed')
		self.parent.parent.firstButtonPressed()
	
	def secondButtonPressed(self):
		print('KivyCustomClassButtons.secondButton pressed')
		self.parent.parent.secondButtonPressed()
	
	def printFirstText(self):
		print('KivyCustomClassButtons.printFirstText() ', self.ids.first_text_input.text)
		self.parent.parent.printFirstText()
	
	def printSecondText(self):
		print('KivyCustomClassButtons.printSecondText() ', self.ids.second_text_input.text)
		self.parent.parent.printSecondText()
