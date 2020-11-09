# Program to explain how to use recycleview in kivy 

import logging
  
# import the kivy module 
from kivy.app import App 
  
# The ScrollView widget provides a scrollable view  
from kivy.uix.recycleview import RecycleView 

from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior


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
	
	def selectItem(self, index):
		_, nodes = self.get_nodes()
		
		if not nodes:
			return
		
		self.select_node(nodes[index])

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
  
# Define the Recycleview class which is created in .kv file 
class AppGUIRecycleView(RecycleView): 
	def __init__(self, **kwargs):
		super(AppGUIRecycleView, self).__init__(**kwargs)

		self.data = [{'text': str(x), 'selectable': True} for x in range(100)]
			
		self.selRBLayout.selectItem(0)
  
# Create the App class with name of your app. 
class RVSampleApp(App): 
	def build(self):
		return AppGUIRecycleView()
  
# run the App 
RVSampleApp().run()