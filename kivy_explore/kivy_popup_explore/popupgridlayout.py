import logging
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.utils import platform

class ConfirmPopup(GridLayout):
	def __init__(self, **kwargs):
		super(ConfirmPopup, self).__init__(**kwargs)

class PopupGridLayoutApp(App):
	def build(self):
		content = ConfirmPopup()
		
		if platform == 'android':
			popupSize = (980, 450)
		elif platform == 'win':
			popupSize = (400, 300)
		
		self.popup = Popup(title="SPLIT AUDIO FILE",
		                   content=content,
		                   size_hint=(None, None),
		                   size=popupSize,
		                   auto_dismiss=False)
		self.popup.open()
	
	def _on_answer(self, instance, answer):
		logging.info("USER ANSWER: {}".format(repr(answer)))
		self.popup.dismiss()


if __name__ == '__main__':
	PopupGridLayoutApp().run()