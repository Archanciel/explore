from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class UsingKivyCustomClassGUI(BoxLayout):
	pass

class KivyCustomClassExploreApp(App):
	def build(self):
		Builder.load_file('kivycustomclassgui.kv')
		
		return UsingKivyCustomClassGUI()


KivyCustomClassExploreApp().run()
