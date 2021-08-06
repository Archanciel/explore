from kivycustomclassspinner import KivyCustomClassSpinner

class KivyCustomClassFields(KivyCustomClassSpinner):
	def __init__(self, **kwargs):
		super(KivyCustomClassFields, self).__init__(**kwargs)
	
	def printFirstText(self):
		print('KivyCustomClassFields.printFirstText() ', self.ids.first_text_input.text)
	
	def printSecondText(self):
		print('KivyCustomClassFields.printSecondText() ', self.ids.second_text_input.text)
	
	def firstButtonPressed(self):
		# calling appGUI method
		self.parent.parent.firstButtonPressed()
		
		print('KivyCustomClassFields.firstButton pressed')
		super().firstButtonPressed()
	
	def secondButtonPressed(self):
		# calling appGUI method
		self.parent.parent.secondButtonPressed()

		print('KivyCustomClassFields.secondButton pressed')
		super(KivyCustomClassFields, self).secondButtonPressed()

	def spinnerValueSet(self):
		# calling appGUI method
		spinnerTextSet = self.ids.spinner_instance.text
		self.parent.parent.spinnerValueSet(spinnerTextSet)

		print('KivyCustomClassFields.spinnerValueSet()')
		super().spinnerValueSet()
