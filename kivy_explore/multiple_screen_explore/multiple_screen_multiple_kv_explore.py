from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.clipboard import Clipboard

# tutorial video: https://youtu.be/xaYn4XdieCs

class MainWindow(Screen):
	def printClipboard(self, clipboardContent):
		print('Clipboard content\n')
		print(clipboardContent)

class SecondWindow(Screen):
	pass


class WindowManager(ScreenManager):
	pass


class MyMainApp(App):
	def build(self):
		Builder.load_file("mainwindow.kv")
		Builder.load_file("secondwindow.kv")
		kv = Builder.load_file("windowmanager.kv")
		
		self.mainWindow = MainWindow()
		
		return kv

	def on_start(self):
		print("Executing MyMainApp.on_start()")
		
		clipboardContent = Clipboard.paste()

		self.mainWindow.printClipboard(clipboardContent)

if __name__ == "__main__":
	MyMainApp().run()