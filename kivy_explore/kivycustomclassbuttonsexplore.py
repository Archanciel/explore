from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class UsingKivyCustomClassGUI(BoxLayout):
	pass

class KivyCustomClassButtonsExploreApp(App):
	def build(self):
		Builder.load_file('kivycustomclassbuttons.kv')
		
		return UsingKivyCustomClassGUI()


KivyCustomClassButtonsExploreApp().run()
