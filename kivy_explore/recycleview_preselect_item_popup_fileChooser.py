import os, logging
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
from kivy.utils import platform

class FileChooserPopup(BoxLayout):
	text = StringProperty()
	
	def __init__(self, rootGUI, **kwargs):
		self.register_event_type('on_answer')
		super(FileChooserPopup, self).__init__(**kwargs)
		self.rootGUI = rootGUI
		
		if os.name != 'posix':
			import string
			available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
			
			self.pathList.data.append({'text': 'Data file location setting', 'selectable': True, 'path': 'c:\\temp\\cpdata'})

			for drive in available_drives:
				self.pathList.data.append({'text': drive, 'selectable': True, 'path': drive})

			# sizing FileChooserPopup widgets
			self.popupBoxLayout.size_hint_y = 0.17
			self.choosenFileText.size_hint_y = 0.12
		else:
			self.pathList.data.append({'text': 'Data file location setting', 'selectable': True, 'path': '/storage/emulated/0/download/Audiobooks'})
			self.pathList.data.append({'text': 'Smartphone', 'selectable': True, 'path': '/storage/emulated/0'})
			self.pathList.data.append({'text': 'SD card', 'selectable': True, 'path': '/storage/0000-0000'})
			
			# sizing FileChooserPopup widgets
			self.popupBoxLayout.size_hint_y = 0.16
			self.choosenFileText.size_hint_y = 0.08

		# specify pre-selected node by its index in the data
		self.diskRecycleBoxLayout.selected_nodes = [0]

	def load(self, path, filename):
		if not filename:
			# no file selected. Load dialog remains open ..
			return

		pathFileName = os.path.join(path, filename[0])
		self.rootGUI.loadFile(pathFileName)
		self.rootGUI.dismissPopup()

	def cancel(self):
		self.rootGUI.dismissPopup()

	def on_answer(self, *args):
		pass

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

class RVPreselItemPopupFileChooserApp(App):
	def build(self):

		if os.name != 'posix':
			# running app om Windows
			Config.set('graphics', 'width', '600')
			Config.set('graphics', 'height', '500')
			Config.write()

		fileChooser = FileChooserPopup(self, text='Do You Love Kivy ?')
		fileChooser.bind(on_answer=self._on_answer)
		
		if platform == 'android':
			popupSize = (1280, 1450) # tablet
			popupSize = (1060, 1450) # smartphone
		elif platform == 'win':
			popupSize = (500, 450)

		self.popup = Popup(title="Answer Question",
		                   content=fileChooser,
		                   size_hint=(None, None),
		                   size=popupSize,
		                   auto_dismiss=False)
			
		self.popup.open()
		
	def loadFile(self, pathFileName):
		import logging
		
		logging.info('loadFile ' + pathFileName)

	def dismissPopup(self):
		self.popup.dismiss()

	def _on_answer(self, instance, answer):
		logging.info("USER ANSWER: {}".format(repr(answer)))
		self.popup.dismiss()
	
RVPreselItemPopupFileChooserApp().run()