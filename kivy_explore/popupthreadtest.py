import time, threading

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout

class AsynchWorker:
	def __init__(self, textInOutGUI):
		self.textInOutGUI = textInOutGUI
		
	def doWork(self):
		for i in range(1, 6):
			time.sleep(1)
			self.textInOutGUI.ids.input.text = '{} seconds'.format(i)
			
		title = 'Please answer'
		msg = 'Restart AsynchWorker ?'
		popup = self.textInOutGUI.createConfirmPopup(title, msg)
		popup.open()

class ConfirmPopup(GridLayout):
	text = StringProperty()
	
	def __init__(self, **kwargs):
		self.register_event_type('on_answer')
		super(ConfirmPopup, self).__init__(**kwargs)
	
	def on_answer(self, *args):
		pass

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
		
		confirmPopup = ConfirmPopup(text=confirmPopupMsg)
		confirmPopup.bind(on_answer=self._on_answer)
		self.popup = Popup(title=confirmPopupTitle,
		                   content=confirmPopup,
		                   size_hint=(None, None),
		                   pos_hint={'top': 0.8},
		                   size=popupSize,
		                   auto_dismiss=False)
		
		return self.popup
	
	def _on_answer(self, instance, answer):
		"""
		This function is called when the user clicks on the Yes or No button
		of the ConfirmPop.
		
		:param instance:
		:param answer: 'Yes' or 'No' string
		
		:return:
		"""
		self.popup.dismiss()
		
		if answer == 'Yes':
			worker = AsynchWorker(self)
			
			t = threading.Thread(target=worker.doWork, args=())
			t.daemon = True
			t.start()
	
	def processInputText(self):
		text = self.ids.input.text
		print(text)
	
	def openConfirmPopup(self):
		title = 'Starting thread choice'
		msg = "Click on Yes to\nlaunch AsynchWorker"
		self.popup = self.createConfirmPopup(title, msg)
		self.popup.open()

# Create the app class
class PopupThreadTest(App):
	# Building text input
	def build(self):
		return KivyGUI()
		
# Run the App which will create the Kivy GUI
if __name__ == "__main__":
	PopupThreadTest().run()
