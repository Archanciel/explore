from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

kv = """
<GuiNoKv>:
	canvas:
		Color:
			rgba: 0.3, 0.3, 0.3, 1
		Rectangle:
			size: self.size
			pos: self.pos
	orientation: 'vertical'
	BoxLayout:
		orientation: 'vertical'
		BoxLayout:
			Button:
				id: next_track
				text: "Next Track"
			Button:
				id: previous_track
				text: "Previous Track"
"""

Builder.load_string(kv)


class GuiNoKv(BoxLayout):
	def __init__(self, **kwargs):
		super(GuiNoKv, self).__init__(**kwargs)
		self.ids.next_track.text = 'NEXT TRACK'

class GuiNoKvApp(App):
	def build(self):
		return GuiNoKv()
	
GuiNoKvApp().run()
