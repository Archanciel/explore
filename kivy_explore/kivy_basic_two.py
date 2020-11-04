from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class GuiTwo(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.loadfile = ObjectProperty(None)
		self.text_input = ObjectProperty(None)
		
		#self.loadBtn.text = 'Coucou'

	def setBtnTxt(self):
		pass
		#self.loadBtn.text = 'COUCOU'

	def on_pause(self):
		# Here you can save data 
		# if needed
		return True

	def on_resume(self):
		# Here you can check if any data
		#needs replacing (usually nothing)
		pass

class GuiTwoApp(App):
	def build(self):  # implicitely looks for
					  # a kv file of name 
					  # guyone.kv which is
					  # class name without App,
					  # in lowercases

		# setting the app dimensions
		if os.name != 'posix':
			# running app om Windows
			Config.set('graphics', 'width', '600')
			Config.set('graphics', 'height', '500')
			Config.write()

if __name__ == '__main__':
	GuiTwoApp().run()
