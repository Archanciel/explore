from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.clipboard import Clipboard



# tutorial video: https://youtu.be/xaYn4XdieCs

class MainWindow(Screen):
	def __init__(self, **kw):
		super().__init__(**kw)
		
		# WARNING: accessing MainWindow fields defined in kv file
		# in the __init__ ctor is no longer possible when using
		# ScreenManager. Here's the solution:
		# (https://stackoverflow.com/questions/26916262/why-cant-i-access-the-screen-ids)
		Clock.schedule_once(self._finish_init)

	def _finish_init(self, dt):
		self.password.text = 'loo'

	def printClipboard(self, clipboardContent):
		print('Clipboard content\n')
		print(clipboardContent)
		
	def switchToSecondScreen(self):
		self.parent.current = "second"
		self.manager.transition.direction = "left"
		
	def doMainWork(self):
		print('MainWindow.doMainWork()')
		

class SecondWindow(Screen):
	def doSecondWork(self):
		print('SecondWindow.doSecondWork()')


class WindowManager(ScreenManager):
	pass


class MyMainApp(App):
	def build(self):
		Builder.load_file("mainwindow.kv")
		Builder.load_file("secondwindow.kv")
		kv = Builder.load_file("windowmanager.kv")
		
		self.mainWindow = MainWindow()
		
		# WARNING: in order for WindowManager to work, its kv file must
		# be returned by the app build() method !
		return kv

	def on_start(self):
		print("Executing MyMainApp.on_start()")
		
		clipboardContent = Clipboard.paste()

		self.mainWindow.printClipboard(clipboardContent)

if __name__ == "__main__":
	MyMainApp().run()