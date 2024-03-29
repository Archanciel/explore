import time, threading

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout

class ConfirmPopupGUIParam(GridLayout):
	"""
	This class is less useful than the ConfirmPopupRegEvent class. The advantage of
	using register_event_type instead of the gui parameter is that the same class can
	be instantiated with binding 'on_answer' to different methods.
	"""
	text = StringProperty()
	
	def __init__(self, gui, displayOptionalButton, **kwargs):
		self.displayOptionalButton = displayOptionalButton
		self.gui = gui
		super(ConfirmPopupGUIParam, self).__init__(**kwargs)
	
	def handleAnswer(self, answer):
		self.gui.handleAnswer(answer)


class KivyGUI(BoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
	def createConfirmPopup(self,
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
		
		confirmPopup = ConfirmPopupGUIParam(gui=self, displayOptionalButton=True, text=confirmPopupMsg)
		self.popup = Popup(title=confirmPopupTitle,
		                   content=confirmPopup,
		                   size_hint=(None, None),
		                   pos_hint={'top': 0.8},
		                   size=popupSize,
		                   auto_dismiss=False)
		
		return self.popup
	
	def handleAnswer(self, answer):
		"""
		This function is called when the user clicks on the Yes or No button
		of the ConfirmPop.
		
		:param answer: 'Yes' or 'No' or 'Optional' string
		
		:return:
		"""
		self.popup.dismiss()
		self.ids.input.text = 'Answer {}'.format(answer)

	def processInputText(self):
		text = self.ids.input.text
		print(text)
	
	def openConfirmPopup(self):
		title = 'Starting thread choice'
		msg = "Click on Yes to\nlaunch AsynchWorker"
		self.popup = self.createConfirmPopup(title, msg)
		self.popup.open()

# Create the app class
class PopupOptionalButtonDisplayUsingGuiParamApp(App):
	# Building text input
	def build(self):
		return KivyGUI()
		
# Run the App which will create the Kivy GUI
if __name__ == "__main__":
	PopupOptionalButtonDisplayUsingGuiParamApp().run()
