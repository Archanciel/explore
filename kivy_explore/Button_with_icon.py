from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<ButtonsApp>:
	orientation: "vertical"
	BoxLayout:
		size_hint_y: 0.1
		Button:
			StackLayout:
				pos: self.parent.pos
				size: self.parent.size
				orientation: 'lr-tb'
				Image:
					source: 'arrow-up-64.png'
					size_hint_x: 1
					width: 74
		Button:
			StackLayout:
				pos: self.parent.pos
				size: self.parent.size
				orientation: 'lr-tb'
				Image:
					source: 'arrow-down-64.png'
					size_hint_x: 1
					width: 74
	BoxLayout:
		size_hint_y: 0.1
		Button:
			StackLayout:
				pos: self.parent.pos
				size: self.parent.size
				orientation: 'lr-tb'
				Image:
					source: 'arrow-up-48.png'
					size_hint_x: 1
					width: 74
		Button:
			StackLayout:
				pos: self.parent.pos
				size: self.parent.size
				orientation: 'lr-tb'
				Image:
					source: 'arrow-down-48.png'
					size_hint_x: 1
					width: 74
	BoxLayout:
		size_hint_y: 0.1
		Button:
			StackLayout:
				pos: self.parent.pos
				size: self.parent.size
				orientation: 'lr-tb'
				Image:
					source: 'arrow-up-32.png'
					size_hint_x: 1
					width: 74
		Button:
			StackLayout:
				pos: self.parent.pos
				size: self.parent.size
				orientation: 'lr-tb'
				Image:
					source: 'arrow-down-32.png'
					size_hint_x: 1
					width: 74
	Label:
		text: "A label"
""")

class ButtonsApp(App, BoxLayout):
	def build(self):
		return self

if __name__ == "__main__":
	ButtonsApp().run()