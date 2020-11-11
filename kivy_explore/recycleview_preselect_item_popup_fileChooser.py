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

class ConfirmPopup(BoxLayout):
	text = StringProperty()
	
	def __init__(self, **kwargs):
		self.register_event_type('on_answer')
		super(ConfirmPopup, self).__init__(**kwargs)
		
		# Set media_list data
		self.medList.data = [{'text': str(x), 'selectable': True} for x in range(100)]
		
		# specify pre-selected node by its index in the data
		self.ctr.selected_nodes = [0]
	
	def on_answer(self, *args):
		pass

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
								 RecycleBoxLayout):
	''' Adds selection and focus behaviour to the view. '''

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


class RVPreselItemPopupFileChooserApp(App):
	def build(self):

		if os.name != 'posix':
			# running app om Windows
			Config.set('graphics', 'width', '600')
			Config.set('graphics', 'height', '500')
			Config.write()

		content = ConfirmPopup(text='Do You Love Kivy ?')
		content.bind(on_answer=self._on_answer)
		
		if platform == 'android':
			popupSize = (1280, 1450)
		elif platform == 'win':
			popupSize = (500, 450)
		
		self.popup = Popup(title="Answer Question",
		                   content=content,
		                   size_hint=(None, None),
		                   size=popupSize,
		                   auto_dismiss=False)
		self.popup.open()
	
	def _on_answer(self, instance, answer):
		logging.info("USER ANSWER: {}".format(repr(answer)))
		self.popup.dismiss()
	
RVPreselItemPopupFileChooserApp().run()