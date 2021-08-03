from kivycustomclassbuttons import KivyCustomClassButtons

class KivyCustomClassFieldsButtons(KivyCustomClassButtons):
	def __init__(self, **kwargs):
		super(KivyCustomClassFieldsButtons, self).__init__(**kwargs)
	
	def printFirstText(self):
		print('KivyCustomClassFieldsButtons.printFirstText() ', self.ids.first_text_input.text)
		super().printFirstText()
	
	def printSecondText(self):
		print('KivyCustomClassFieldsButtons.printSecondText() ', self.ids.second_text_input.text)
		super().printSecondText()
