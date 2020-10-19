from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.utils import platform

Builder.load_string('''
<ConfirmPopup>:
    cols:1
	Label:
		text: root.text
	GridLayout:
		cols: 2
		size_hint_y: None
		height: '28dp'
		Button:
			text: 'Yes'
			on_release: root.dispatch('on_answer','yes')
		Button:
			text: 'No'
			on_release: root.dispatch('on_answer', 'no')
''')


class ConfirmPopup(GridLayout):
	text = StringProperty()
	
	def __init__(self, **kwargs):
		self.register_event_type('on_answer')
		super(ConfirmPopup, self).__init__(**kwargs)
	
	def on_answer(self, *args):
		pass


class PopupTest(App):
	def build(self):
		content = ConfirmPopup(text='Do You Love Kivy?')
		content.bind(on_answer=self._on_answer)
		
		if platform == 'android':
			popupSize = (980, 450)
		elif platform == 'win':
			popupSize = (300, 150)
		
		self.popup = Popup(title="Answer Question",
		                   content=content,
		                   size_hint=(None, None),
		                   size=popupSize,
		                   auto_dismiss=False)
		self.popup.open()
	
	def _on_answer(self, instance, answer):
		print("USER ANSWER: ", repr(answer))
		self.popup.dismiss()


if __name__ == '__main__':
	PopupTest().run()