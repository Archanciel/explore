from kivycustomclassbuttons import KivyCustomClassButtons

class KivyCustomClassSpinner(KivyCustomClassButtons):
	def __init__(self, **kwargs):
		super(KivyCustomClassSpinner, self).__init__(**kwargs)

	def spinnerValueSet(self):
		"""
		Method called by KivyCustomClassFields, sub class of
		KivyCustomClassSpinner.
		"""
		spinnerTextSet = self.ids.spinner_instance.text
		print('KivyCustomClassSpinner.spinnerValueSet() ', spinnerTextSet)
	
	def firstButtonPressed(self):
		"""
		Method called by KivyCustomClassFields, sub class of
		KivyCustomClassSpinner.
		"""
		print('KivyCustomClassSpinner.firstButton pressed')
		super().firstButtonPressed()
	
	def secondButtonPressed(self):
		"""
		Method called by KivyCustomClassFields, sub class of
		KivyCustomClassSpinner.
		"""
		print('KivyCustomClassSpinner.secondButton pressed')
		super(KivyCustomClassSpinner, self).secondButtonPressed()
