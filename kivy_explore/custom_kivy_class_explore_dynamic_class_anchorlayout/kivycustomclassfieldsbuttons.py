from kivy.uix.boxlayout import BoxLayout

# instrution below causes failure on Android !
from kivy_explore.custom_kivy_class_explore_display_doubled.kivycustomclassbuttons import KivyCustomClassButtons

class KivyCustomClassFieldsButtons():
	"""
	Kivy dynamic class inheritance from KivyCustomClassButtons is specified
	in kv file.
	"""
	def __init__(self, **kwargs):
		super(KivyCustomClassFieldsButtons, self).__init__(**kwargs)
	
	def firstButtonPressed(self):
		print('KivyCustomClassFieldsButtons.firstButton pressed')
		self.parent.firstButtonPressed()
	
	def secondButtonPressed(self):
		print('KivyCustomClassFieldsButtons.secondButton pressed')
		self.parent.secondButtonPressed()
	
	def printFirstText(self):
		print('KivyCustomClassFieldsButtons.printFirstText() ', self.ids.first_text_input.text)
		self.parent.printFirstText()
	
	def printSecondText(self):
		print('KivyCustomClassFieldsButtons.printSecondText() ', self.ids.second_text_input.text)
		self.parent.printSecondText()
