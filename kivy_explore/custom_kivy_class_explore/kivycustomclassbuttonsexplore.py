from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class AppGUI(BoxLayout):
	
	def firstButtonPressed(self):
		print('AppGUI.firstButton pressed')
	
	def secondButtonPressed(self):
		print('AppGUI.secondButton pressed')


class KivyCustomClassButtonsExploreApp(App):
	def build(self):
		Builder.load_file('kivycustomclassbuttonslayout.kv')
		
		return AppGUI()


KivyCustomClassButtonsExploreApp().run()
