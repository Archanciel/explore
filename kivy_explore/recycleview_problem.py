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
			return self.parent.select_with_touch(self.index, touch)

	def apply_selection(self, rv, index, is_selected):
		''' Respond to the selection of items in the view. '''
		self.selected = is_selected
		if is_selected:
			print("selection changed to {0}".format(rv.data[index]))
		else:
			print("selection removed for {0}".format(rv.data[index]))

class LoadDialog(FloatLayout):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)
	#drivesListRV = ObjectProperty(None)
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		if os.name != 'posix':
			import string
			available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]


			for drive in available_drives:
				self.drivesListRV.data.append({'text': drive})
		else:
			for i in range(14):
				self.drivesListRV.data.append({'text': str(i)})		
		#self.drivesListRV.data = [{'text': str(x)} for x in range(20)]

class Root(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.loadfile = ObjectProperty(None)
		#self.rvMain = ObjectProperty(None)
		#self.rvMain.data.append({'text': 'hello'})
		#for i in range(4):
		#	self.rvMain.data.append({'text': str(i)})		
		self.rvMain.data = [{'text': str(x)} for x in range(20)] 
		
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Load file", content=content,
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

class RVProblemNoScrollApp(App):
	def build(self):  # implicitely looks for a kv file of name audiodownloadergui.kv which is
					  # class name without App, in lowercases

		# setting the app dimensions
		if os.name != 'posix':
			# running app om Windows
			Config.set('graphics', 'width', '600')
			Config.set('graphics', 'height', '500')
			Config.write()

		return Root()
		
if __name__ == '__main__':
	RVProblemNoScrollApp().run()
