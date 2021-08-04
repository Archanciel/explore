from kivycustomclassbuttons import KivyCustomClassButtons

class KivyCustomClassSpinner(KivyCustomClassButtons):
	def __init__(self, **kwargs):
		super(KivyCustomClassSpinner, self).__init__(**kwargs)

	def spinnerValueSet(self):
		spinnerTextSet = self.ids.spinner_instance.text
		print('KivyCustomClassSpinner.spinnerValueSet() ', spinnerTextSet)
		self.parent.parent.spinnerValueSet(spinnerTextSet)
