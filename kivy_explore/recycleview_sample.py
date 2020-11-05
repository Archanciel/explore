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

	# required to authorise unselecting a selected item
	touch_deselect_last = BooleanProperty(True)

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
		#self.data = [{'text': str(x)} for x in range(50)]
		for i in range(50):
			self.data.append({'text': str(i)})
  
# Create the App class with name of your app. 
class RVSampleApp(App): 
	def build(self):
		return AppGUIRecycleView()
  
# run the App 
RVSampleApp().run() 