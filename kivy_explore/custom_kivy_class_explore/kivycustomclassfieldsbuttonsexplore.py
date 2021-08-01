from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class AppGUI(BoxLayout):
	pass

class KivyCustomClassFieldsButtonsExploreApp(App):
	def build(self):
		Builder.load_file('kivycustomclassfieldsbuttons.kv')
		Builder.load_file('kivycustomclassbuttons.kv')

		return AppGUI()


KivyCustomClassFieldsButtonsExploreApp().run()
