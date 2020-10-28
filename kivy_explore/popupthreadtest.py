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
		for i in range(1, 11):
			time.sleep(1)
			self.textInOutGUI.ids.input.text = '{} seconds'.format(i)
			
		self.textInOutGUI.createAndOpenConfirmPopup('Please answer', 'Restart AsynchWorker ?', self.doWork)

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
	                       confirmPopupMsg,
	                       newThreadAsynchCallbackFunction):
		"""

		:param confirmPopupTitle:
		:param confirmPopupMsg:
		:param newThreadAsynchCallbackFunction: function called when the user click on
											 yes or no button
		:return:
		"""
		self.newThreadAsynchCallbackFunction = newThreadAsynchCallbackFunction
		
		popupSize = None
		
		if platform == 'android':
			popupSize = (980, 600)
		elif platform == 'win':
			popupSize = (200, 150)
		
		confirmPopup = ConfirmPopup(text=confirmPopupMsg)
		confirmPopup.bind(on_answer=self._on_answer)
		popup = Popup(title=confirmPopupTitle,
		              content=confirmPopup,
		              size_hint=(None, None),
		              pos_hint={'top': 0.8},
		              size=popupSize,
		              auto_dismiss=False)
		
		return popup
	
	def createAndOpenConfirmPopup(self, title, msg, callback):
		self.popup = self.createConfirmPopup(title, msg, callback)
		self.popup.open()
	
	def _on_answer(self, instance, answer):
		print("USER ANSWER: ", repr(answer))
		
		self.popup.dismiss()
		
		if answer == 'Yes':
			t = threading.Thread(target=self.newThreadAsynchCallbackFunction, args=())
			t.daemon = True
			t.start()
	
	def processInputText(self):
		text = self.ids.input.text
		print(text)
	
	def openConfirmPopup(self):
		worker = AsynchWorker(self)
		self.createAndOpenConfirmPopup('Starting thread choice', "Click on Yes to\nlaunch AsynchWorker", worker.doWork)

# Create the app class
class PopupThreadTest(App):
	# Building text input
	def build(self):
		return KivyGUI()
		
# Run the App which will create the Kivy GUI
if __name__ == "__main__":
	PopupThreadTest().run()
