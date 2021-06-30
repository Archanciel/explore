import logging
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

# RecycleView related imports
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

import os

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
								 RecycleBoxLayout):
	''' Adds selection and focus behaviour to the view. '''

	# required to forbid unselecting a selected item. An item can be unselected
	# only by selecting another item
	touch_deselect_last = BooleanProperty(False)

class SelectableLabel(RecycleDataViewBehavior, Label):
	''' Add selection support to the Label '''
	index = None
	selected = BooleanProperty(False)
	selectable = BooleanProperty(True)

	def refresh_view_attrs(self, rv, index, data):
		''' Catch and handle the view changes '''
		self.index = index
		return super(SelectableLabel, self).refresh_view_attrs(
			rv, index, data)

	def on_touch_down(self, touch):
		''' Add selection on touch down '''
		if super(SelectableLabel, self).on_touch_down(touch):
			return True
		if self.collide_point(*touch.pos) and self.selectable:
			# the parent is the containing SelectableRecycleBoxLayout.
			# If the container is simply a RecycleBoxLayout,
			# an error will occur since the RecycleBoxLayout has
			# no method select_with_touch(), method which was
			# added by the class LayoutSelectionBehavior
			return self.parent.select_with_touch(self.index, touch)

	def apply_selection(self, rv, index, is_selected):
		''' Respond to the selection of items in the view. '''
		
		if not self.selected and not is_selected:
			# case when adding a new list item
			logging.info('simply return {}'.format(index))
			return
		elif self.selected and not is_selected:
			# toggling from selected to unselected
			logging.info('handling deselection {}'.format(index))
			self.selected = False
			#rv.parent.parent.recycleViewSelectItem(index, is_selected)
		else:
			# toggling from unselected to selected
			self.selected = not self.selected
			logging.info('handling selection {}'.format(index))

class LoadDialog(FloatLayout):
	text_path_load = ObjectProperty(None)
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		if os.name != 'posix':
			import string
			available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

			for drive in available_drives:
				self.drivesListRV.data.append({'text': drive, 'selectable': True})
				
			# specify pre-selected node by its index in the data
			self.selRbLayout.selected_nodes = [0]
		else:
			self.drivesListRV.data.append({'text': 'main', 'selectable': True})
			self.drivesListRV.data.append({'text': 'sd card', 'selectable': True})
		
			# specify pre-selected node by its index in the data
			self.selRbLayout.selected_nodes = [0]
	
	# There's a dependency between the range size value and the height
			# of list line !!!!
			# for i in range(3):
			# 	self.drivesListRV.data.append({'text': str(i)})
		
		# not working self.ids.controller.selectItem(0)

class FileChooserSelOrCreateDirGUI(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.loadfile = ObjectProperty(None)
		self.text_input = ObjectProperty(None)
		
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = LoadDialog(load=self.selectOrCreateDir, cancel=self.dismiss_popup)
		self._popup = Popup(title="Load file", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()
		# not working content.ids.controller.selectItem(0)

	def selectOrCreateDir(self, textPathLoad):
		if os.path.isfile(textPathLoad):
			print("{} file was selected".format(textPathLoad))
		elif os.path.isdir(textPathLoad):
			print("{} dir was selected".format(textPathLoad))
		else:
			try:
				os.mkdir(textPathLoad)
				print("{} dir was created".format(textPathLoad))
			except FileExistsError as e:
				print("{} dir already exists".format(textPathLoad))
		
		self.dismiss_popup()

	def on_pause(self):
		# Here you can save data if needed
		return True

	def on_resume(self):
		# Here you can check if any data needs replacing (usually nothing)
		pass


class FileChooserSelOrCreateDirApp(App):
	def build(self):  # implicitely looks for a kv file of name audiodownloadergui.kv which is
					  # class name without App, in lowercases

		# setting the app dimensions
		if os.name != 'posix':
			# running app om Windows
			Config.set('graphics', 'width', '600')
			Config.set('graphics', 'height', '500')
			Config.write()


if __name__ == '__main__':
	FileChooserSelOrCreateDirApp().run()
