from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class UsingKivyCustomClassEmbededGUI(BoxLayout):
	pass

class KivyCustomClassEmbededExploreApp(App):
	def build(self):
		Builder.load_file('kivycustomclassfieldsbuttons.kv')
		
		return UsingKivyCustomClassEmbededGUI()


KivyCustomClassEmbededExploreApp().run()
