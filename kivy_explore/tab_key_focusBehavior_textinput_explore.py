from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class FocusTextInput(TextInput):
	"""
	This class replaces the TextInput class in the .kv files in order
	to enable using TAB to move from one TextInput field to the next
	one.

	In order for TAB to cycle through the TextIput fields, all the
	formulary TextInput fields must be replaced by FocusTextInput.

	WARNING:

	Defining class FocusTextInput(FocusBehavior, TextInput)
	raises a TypeError: Cannot create a consistent method resolution
	 order (MRO) for bases FocusBehavior, TextInput.

	The reason is that TextInput already inherits from FocusBehavior.
	"""
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.multiline = False
	
	def keyboard_on_key_down(self, window, keycode, text, modifiers):
		if keycode[1] == 'tab':
			self.get_focus_next().focus = True
		else:
			super().keyboard_on_key_down(window, keycode, text, modifiers)
		
	def on_focus(self, instance, value, *largs):
		# self.get_focus_previous().background_color = 1.0, 1.0, 1.0, 1.0
		# self.background_color = 1.0, 0.0, 0.0, 1.0
		if value == True:
			print(self.text)

class FocusBehaviorGUI(GridLayout):
	def __init__(self, **kwargs):
		super().__init__( **kwargs)

		self.cols = 4
		self.rows = 2
		
		for i in range(8):
			self.add_widget(FocusTextInput(text=str(i)))

class FocusBehaviorApp(App):
	def build(self):
		return FocusBehaviorGUI()

if __name__ == '__main__':
	FocusBehaviorApp().run()