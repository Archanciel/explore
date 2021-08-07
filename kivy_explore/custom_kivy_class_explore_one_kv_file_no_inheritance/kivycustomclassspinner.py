from kivy.uix.boxlayout import BoxLayout


class KivyCustomClassSpinner(BoxLayout):
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
	
	def secondButtonPressed(self):
		"""
		Method called by KivyCustomClassFields, sub class of
		KivyCustomClassSpinner.
		"""
		print('KivyCustomClassSpinner.secondButton pressed')
