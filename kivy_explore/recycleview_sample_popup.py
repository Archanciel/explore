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
from kivy.uix.floatlayout import FloatLayout
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
			
class RecycleViewForPopup(RecycleView):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		super(RecycleViewForPopup, self).__init__(**kwargs)
		
		if os.name != 'posix':
			import string
			available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]


			for drive in available_drives:
				self.data.append({'text': drive})
		else:
			for i in range(50):
				self.data.append({'text': str(i)})		
		#self.drivesListRV.data = [{'text': str(x)} for x in range(20)]
  
class AppGUI(FloatLayout): 
	def __init__(self, **kwargs):
		super(AppGUI, self).__init__(**kwargs)
		
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = RecycleViewForPopup(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="RecycleView in Popup", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()
		
	def load(self, path, filename):

		self.dismiss_popup()

	def on_pause(self):
		# Here you can save data if needed
		return True

	def on_resume(self):
		# Here you can check if any data needs replacing (usually nothing)
		pass
  
# Create the App class with name of your app. 
class RVSamplePopupApp(App): 
	def build(self):
		return AppGUI()
  
# run the App 
RVSamplePopupApp().run() 