from kivy.uix.boxlayout import BoxLayout


class Box1(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def button_one_pressed(self):
		print('Box1.button_one_pressed()')