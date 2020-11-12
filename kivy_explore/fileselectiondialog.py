import os, logging
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, StringProperty, NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup
from kivy.utils import platform

class FileSelectionPopupContent(BoxLayout):
	
	def __init__(self, **kwargs):
		super(FileSelectionPopupContent, self).__init__(**kwargs)
		
		self.register_event_type('on_answer')

		if os.name != 'posix':
			import string
			available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

			for drive in available_drives:
				self.medList.data.append({'text': drive, 'selectable': True})
		else:
			self.medList.data.append({'text': 'main', 'selectable': True})
			self.medList.data.append({'text': 'sd card', 'selectable': True})
		
		# specify pre-selected node by its index in the data
		self.selRBLayout.selected_nodes = [0]
	
	def on_answer(self, *args):
		pass

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
								 RecycleBoxLayout):
								 	
	# required to forbid unselecting a selected item. An item can be unselected
	# only by selecting another item
	touch_deselect_last = BooleanProperty(False)

	def get_nodes(self):
		nodes = self.get_selectable_nodes()
		if self.nodes_order_reversed:
			nodes = nodes[::-1]
		if not nodes:
			return None, None
		
		selected = self.selected_nodes
		if not selected:  # nothing selected, select the first
			self.select_node(nodes[0])
			return None, None
		
		if len(nodes) == 1:  # the only selectable node is selected already
			return None, None
		
		last = nodes.index(selected[-1])
		self.clear_selection()
		return last, nodes
	
	
	def select_next(self):
		last, nodes = self.get_nodes()
		if not nodes:
			return
		
		if last == len(nodes) - 1:
			self.select_node(nodes[0])
		else:
			self.select_node(nodes[last + 1])
	
	
	def select_previous(self):
		last, nodes = self.get_nodes()
		if not nodes:
			return
		
		if not last:
			self.select_node(nodes[-1])
		else:
			self.select_node(nodes[last - 1])

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
			logging.info("selection changed to {0}".format(rv.data[index]))
		else:
			logging.info("selection removed for {0}".format(rv.data[index]))

class Root(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.loadfile = ObjectProperty(None)
		self.text_input = ObjectProperty(None)
		
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = FileSelectionPopupContent()
		content.bind(on_answer=self._on_answer)
		
		if platform == 'android':
			popupSize = (1280, 1450) # tablet
			popupSize = (1060, 1450) # smartphone
		elif platform == 'win':
			popupSize = (500, 450)
		
		self.popup = Popup(title="Go on with file selection ...",
		                   content=content,
		                   size_hint=(None, None),
		                   size=popupSize,
		                   auto_dismiss=False)
		self.popup.open()
	
	def _on_answer(self, instance, answer):
		logging.info("USER ANSWER: {}".format(repr(answer)))
		self.popup.dismiss()

	def load(self, path, filename):
		with open(os.path.join(path, filename[0])) as stream:
			self.text_input.text = stream.read()

		self.dismiss_popup()

	def on_pause(self):
		# Here you can save data if needed
		return True

	def on_resume(self):
		# Here you can check if any data needs replacing (usually nothing)
		pass

class FileSelectionDialogApp(App):
	def build(self):

		if os.name != 'posix':
			# running app om Windows
			Config.set('graphics', 'width', '600')
			Config.set('graphics', 'height', '500')
			Config.write()

	
FileSelectionDialogApp().run()