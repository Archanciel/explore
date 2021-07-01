from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# tutorial video: https://youtu.be/xaYn4XdieCs

class MainWindow(Screen):
	pass


class SecondWindow(Screen):
	pass


class WindowManager(ScreenManager):
	pass


class MyMainApp(App):
	def build(self):
		Builder.load_file("mainwindow.kv")
		Builder.load_file("secondwindow.kv")
		kv = Builder.load_file("windowmanager.kv")
		
		return kv


if __name__ == "__main__":
	MyMainApp().run()