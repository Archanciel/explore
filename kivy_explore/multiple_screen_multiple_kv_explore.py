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


kv = Builder.load_file("multiple_screen_multiple_kv_explore.kv")


class MyMainApp(App):
	def build(self):
		return kv


if __name__ == "__main__":
	MyMainApp().run()