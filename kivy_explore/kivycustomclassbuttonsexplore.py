from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class AppGUI(BoxLayout):
	pass

class KivyCustomClassButtonsExploreApp(App):
	def build(self):
		Builder.load_file('kivycustomclassbuttons.kv')
		
		return AppGUI()


KivyCustomClassButtonsExploreApp().run()
