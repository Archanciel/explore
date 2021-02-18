# Multiple .kv file Python code

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
from kivy_explore.mulkvfilesbox1 import Box1

Builder.load_file('mulkvfilesbox1.kv')
Builder.load_file('mulkvfilesbox2.kv')


# Creating main kv file class
class MulKvFiles(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.box1 = Box1()


# Create App class
class MulKvFilesApp(App):
	def build(self):
		self.x = 150
		self.y = 400
		return MulKvFiles()

# run the App


if __name__ == '__main__':
	MulKvFilesApp().run()