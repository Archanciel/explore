import kivy

# Source code obtained from GeeksForGeeks article
# https://www.geeksforgeeks.org/python-how-to-use-multiple-kv-files-in-kivy/

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# The GridLayout arranges children in a matrix.
# It takes the available space and divides
# it into columns and rows, then adds
# widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout

# Builder is a global Kivy instance used
# in widgets that you can use to load other
# kv files in addition to the default ones.
from kivy.lang import Builder

# Loading Multiple .kv files
Builder.load_file('box1.kv')
Builder.load_file('box2.kv')
Builder.load_file('box3.kv')


# Creating main kv file class
class MainMultipleKvFileGUI(GridLayout):
	pass


# Create App class
class MainMultipleKvFileApp(App):
	def build(self):
		self.x = 150
		self.y = 400
		return MainMultipleKvFileGUI()


# run the App
if __name__ == '__main__':
	MainMultipleKvFileApp().run()