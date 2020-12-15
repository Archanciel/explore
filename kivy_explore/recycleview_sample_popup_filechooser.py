# Program to explain how to use recycleview in kivy 

import logging, os
  
# import the kivy module 
from kivy.app import App 
  
# The ScrollView widget provides a scrollable view  
from kivy.uix.recycleview import RecycleView 
from kivy.uix.popup import Popup

from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

SD_CARD_DIR_TABLET = '/storage/0000-0000'
SD_CARD_DIR_SMARTPHONE = '/storage/9016-4EF8'

class SelectableRecycleBoxLayoutFileChooser(FocusBehavior, LayoutSelectionBehavior,
								 RecycleBoxLayout):
	''' Adds selection and focus behaviour to the view. '''

	# required to authorise unselecting a selected item
	touch_deselect_last = BooleanProperty(True)

class SelectableLabelFileChooser(RecycleDataViewBehavior, Label):
	''' Add selection support to the Label '''
	index = None
	selected = BooleanProperty(False)
	selectable = BooleanProperty(True)
	
	def refresh_view_attrs(self, rv, index, data):
		''' Catch and handle the view changes '''
		self.index = index
		return super(SelectableLabelFileChooser, self).refresh_view_attrs(
			rv, index, data)
	
	def on_touch_down(self, touch):
		''' Add selection on touch down '''
		if super(SelectableLabelFileChooser, self).on_touch_down(touch):
			return True
		if self.collide_point(*touch.pos) and self.selectable:
			return self.parent.select_with_touch(self.index, touch)
	
	def apply_selection(self, rv, index, is_selected):
		''' Respond to the selection of items in the view. '''
		self.selected = is_selected
		
		if is_selected:
			rootGUI = rv.parent.parent
			selectedPath = rv.data[index]['path']
			
			if os.name != 'posix':
				# we are on Windows
				selectedPath = selectedPath + '\\'  # adding '\\' is required,otherwise,
			# when selecting D:, the directory
			# hosting the utility is selected !
			
			rootGUI.fileChooser.path = selectedPath
			rootGUI.currentPathField.text = selectedPath

class FileChooserPopup(BoxLayout):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
	def __init__(self, rootGUI, **kwargs):
		super(FileChooserPopup, self).__init__(**kwargs)
		
		self.rootGUI = rootGUI
		
		if os.name != 'posix':
			import string
			available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
			
			self.pathList.data.append(
				{'text': 'Data file location setting', 'selectable': True, 'path': 'c:\\temp\\cpdata'})
			
			for drive in available_drives:
				self.pathList.data.append({'text': drive, 'selectable': True, 'path': drive})
			
			# sizing FileChooserPopup widgets
			self.popupBoxLayout.size_hint_y = 0.17
			self.currentPathField.size_hint_y = 0.12
		else:
			self.pathList.data.append({'text': 'Data file location setting', 'selectable': True,
			                           'path': '/storage/emulated/0/download/Audiobooks'})
			self.pathList.data.append({'text': 'Main RAM', 'selectable': True, 'path': '/storage/emulated/0'})
			
			sdCardDir = SD_CARD_DIR_SMARTPHONE
			
			if not os.path.isdir(sdCardDir):
				sdCardDir = SD_CARD_DIR_TABLET
			
			self.pathList.data.append({'text': 'SD card', 'selectable': True, 'path': sdCardDir})
			
			# sizing FileChooserPopup widgets
			self.popupBoxLayout.size_hint_y = 0.16
			self.currentPathField.size_hint_y = 0.08
		
		# specify pre-selected node by its index in the data
		self.diskRecycleBoxLayout.selected_nodes = [0]


class AppGUI(FloatLayout): 
	def __init__(self, **kwargs):
		super(AppGUI, self).__init__(**kwargs)
		
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = FileChooserPopup(rootGUI=self, load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="RecycleView in Popup", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()
		
	def load(self, path, filename):
		pathFileName = os.path.join(path, filename[0])

		import logging
		logging.info('loadFile ' + pathFileName)
	
	def on_pause(self):
		# Here you can save data if needed
		return True

	def on_resume(self):
		# Here you can check if any data needs replacing (usually nothing)
		pass
  
# Create the App class with name of your app. 
class RVSamplePopupFileChooserApp(App):
	def build(self):
		return AppGUI()
  
# run the App 
RVSamplePopupFileChooserApp().run()