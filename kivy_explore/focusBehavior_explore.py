from kivy.app import App
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class FocusButton(FocusBehavior, Button):
	def _on_focus(self, instance, value, *largs):
		print(self.text)

class FocusBehaviorGUI(GridLayout):
	def __init__(self, **kwargs):
		super().__init__( **kwargs)

		self.cols = 4
		self.rows = 2
		
		for i in range(8):
			self.add_widget(FocusButton(text=str(i)))
		# clicking on a widget will activate focus, and tab can now be used
		# to cycle through

class FocusBehaviorApp(App):
	def build(self):
		return FocusBehaviorGUI()

if __name__ == '__main__':
	FocusBehaviorApp().run()