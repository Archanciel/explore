from kivy.uix.boxlayout import BoxLayout

from kivy_explore.custom_kivy_class_explore.kivycustomclassbuttons import KivyCustomClassButtons


class KivyCustomClassFieldsButtons(KivyCustomClassButtons):
	def __init__(self, **kwargs):
		super(KivyCustomClassFieldsButtons, self).__init__(**kwargs)
		
	def printFirstText(self):
		print(self.ids.first_text_input.text)
	
	def printSecondText(self):
		print(self.ids.second_text_input.text)
