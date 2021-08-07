from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class AppGUI(BoxLayout):
	
	def firstButtonPressed(self):
		print('AppGUI.firstButton pressed')
	
	def secondButtonPressed(self):
		print('AppGUI.secondButton pressed')
	
	def printFirstText(self):
		print('AppGUI.printFirstText() ', self.ids.custom_class_fields_instance.ids.first_text_input.text)
	
	def printSecondText(self):
		print('AppGUI.printSecondText() ', self.ids.custom_class_fields_instance.ids.second_text_input.text)

	def spinnerValueSet(self, spinnerTextSet):
		initialText = self.ids.custom_class_fields_instance.ids.first_text_input.text
		self.ids.custom_class_fields_instance.ids.first_text_input.text = initialText + " " + spinnerTextSet
		print('AppGUI.spinnerValueSet() executed, which updated first text input field !')


class KivyCustomClassExploreOneKvApp(App):
	def build(self):
		# IMPORTANT: the order of loading the kv files determines the
		# order in which the kv content is displayed.
		# Builder.load_file('kivycustomclassfields.kv')
		# Builder.load_file('kivycustomclassspinner.kv')
		# Builder.load_file('kivycustomclassbuttons.kv')

		return AppGUI()


KivyCustomClassExploreOneKvApp().run()
