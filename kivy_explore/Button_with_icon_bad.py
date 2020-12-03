from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ButtonsApp>:
	orientation: "vertical"
	BoxLayout:
		orientation: "vertical"
		Button:
			size_hint_y: 0.1
			Image:
				source: 'kivy.png'
				y: ((self.parent.y + self.parent.height)) - 150
				x: ((self.parent.x + self.parent.width) / 2) - 50
		Label:
			text: "A label"
""")

class ButtonsApp(App, BoxLayout):
	def build(self):
		return self

if __name__ == "__main__":
	ButtonsApp().run()