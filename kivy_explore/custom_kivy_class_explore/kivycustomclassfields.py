from kivycustomclassbuttons import KivyCustomClassButtons

class KivyCustomClassFields(KivyCustomClassButtons):
	def __init__(self, **kwargs):
		super(KivyCustomClassFields, self).__init__(**kwargs)
	
	def printFirstText(self):
		print('KivyCustomClassFields.printFirstText() ', self.ids.first_text_input.text)
		super().printFirstText()
	
	def printSecondText(self):
		print('KivyCustomClassFields.printSecondText() ', self.ids.second_text_input.text)
		super().printSecondText()
