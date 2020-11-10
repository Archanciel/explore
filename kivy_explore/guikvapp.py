from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class GuiKv(BoxLayout):
	def __init__(self, **kwargs):
		super(GuiKv, self).__init__(**kwargs)
		self.ids.next_track.text = 'NEXT TRACK'
		
class GuiKvApp(App):
	def build(self):
		return GuiKv()
	
GuiKvApp().run()
