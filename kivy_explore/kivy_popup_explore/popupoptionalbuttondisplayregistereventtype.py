import time, threading

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout

class ConfirmPopup(GridLayout):
	"""
	The advantage of using register_event_type is that the same class can be
	instantiated with binding 'on_answer' to different methods.
	"""
	text = StringProperty()
	
	def __init__(self, displayOptionalButton, **kwargs):
		self.register_event_type('on_answer')
		self.displayOptionalButton = displayOptionalButton
		super(ConfirmPopup, self).__init__(**kwargs)

	def on_answer(self, *args):
		pass

class KivyGUI(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def createConfirmPopupOptButton(self,
	                                confirmPopupTitle,
	                                confirmPopupMsg):
		"""

		:param confirmPopupTitle:
		:param confirmPopupMsg:

		:return:
		"""
		popupSize = None
		
		if platform == 'android':
			popupSize = (980, 600)
		elif platform == 'win':
			popupSize = (200, 150)
		
		confirmPopup = ConfirmPopup(displayOptionalButton=True, text=confirmPopupMsg)
		confirmPopup.bind(on_answer=self._on_answer_optButton)
		self.popup = Popup(title=confirmPopupTitle,
		                   content=confirmPopup,
		                   size_hint=(None, None),
		                   pos_hint={'top': 0.8},
		                   size=popupSize,
		                   auto_dismiss=False)
		
		return self.popup
	
	def createConfirmPopupNoOptButton(self,
	                                  confirmPopupTitle,
	                                  confirmPopupMsg):
		"""

		:param confirmPopupTitle:
		:param confirmPopupMsg:

		:return:
		"""
		popupSize = None
		
		if platform == 'android':
			popupSize = (980, 600)
		elif platform == 'win':
			popupSize = (200, 150)
		
		confirmPopup = ConfirmPopup(displayOptionalButton=False, text=confirmPopupMsg)
		confirmPopup.bind(on_answer=self._on_answer_noOptButton)
		self.popup = Popup(title=confirmPopupTitle,
		                   content=confirmPopup,
		                   size_hint=(None, None),
		                   pos_hint={'top': 0.8},
		                   size=popupSize,
		                   auto_dismiss=False)
		
		return self.popup
	
	def _on_answer_optButton(self, instance, answer):
		"""
		This function is called when the user clicks on the Yes or No button
		of the ConfirmPop.
		
		:param instance:
		:param answer: 'Yes' or 'No' string
		
		:return:
		"""
		self.popup.dismiss()
		self.ids.input.text = 'Answer {}'.format(answer)
	
	def _on_answer_noOptButton(self, instance, answer):
		"""
		This function is called when the user clicks on the Yes or No button
		of the ConfirmPop.

		:param instance:
		:param answer: 'Yes' or 'No' string

		:return:
		"""
		self.popup.dismiss()
		self.ids.input.text = 'Answer {}'.format(answer).upper()
	
	def processInputText(self):
		text = self.ids.input.text
		print(text)
	
	def openConfirmPopupOptButton(self):
		title = 'Starting thread choice'
		msg = "Click on Yes to\nlaunch AsynchWorker"
		self.popup = self.createConfirmPopupOptButton(title, msg)
		self.popup.open()
	
	def openConfirmPopupNoOptButton(self):
		title = 'Starting thread choice'
		msg = "Click on Yes to\nlaunch AsynchWorker"
		self.popup = self.createConfirmPopupNoOptButton(title, msg)
		self.popup.open()


# Create the app class
class PopupOptionalButtonDisplayRegisterEventTypeApp(App):
	# Building text input
	def build(self):
		return KivyGUI()
		
# Run the App which will create the Kivy GUI
if __name__ == "__main__":
	PopupOptionalButtonDisplayRegisterEventTypeApp().run()
