import logging
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.utils import platform

class ConfirmPopup(GridLayout):
	text = StringProperty()
	
	def __init__(self, gui, **kwargs):
		self.register_event_type('on_answer')
		super(ConfirmPopup, self).__init__(**kwargs)
		
		self.gui = gui
		
	def yes(self):
		self.gui.processYes()
	
	def no(self):
		self.gui.processNo()

class PopupTestUsingGuiParamApp(App):
	def build(self):
		content = ConfirmPopup(gui=self,
		                       text='Do You Love Kivy long line long line line\nSecond line\nThird line')
		
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
		
	def processYes(self):
		print('Button yes pressed')
		self.popup.dismiss()
	
	def processNo(self):
		print('Button no pressed')
		self.popup.dismiss()


if __name__ == '__main__':
	PopupTestUsingGuiParamApp().run()