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
	text_path_load = ObjectProperty(None)
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)

class Root(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.loadfile = ObjectProperty(None)
		self.text_input = ObjectProperty(None)
		
	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self):
		content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
		
		import os, string
		available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

		content.drivesListRV.data.append({'text': available_drives[0]})
		content.drivesListRV.data.append({'text': available_drives[1]})
		content.drivesListRV.data.append({'text': available_drives[0]})
		content.drivesListRV.data.append({'text': available_drives[1]})
#		content.drivesListRV.data = [{'text': str(x)} for x in available_drives]

		self._popup = Popup(title="Load file", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()

	def show_save(self):
		content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
		self._popup = Popup(title="Save file", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()

	def load(self, path, filename):
		with open(os.path.join(path, filename[0])) as stream:
			self.text_input.text = stream.read()

		self.dismiss_popup()

	def save(self, path, filename):
		with open(os.path.join(path, filename), 'w') as stream:
			stream.write(self.text_input.text)

		self.dismiss_popup()

	def on_pause(self):
		# Here you can save data if needed
		return True

	def on_resume(self):
		# Here you can check if any data needs replacing (usually nothing)
		pass

class FileChooserEditorApp(App):
	def build(self):  # implicitely looks for a kv file of name audiodownloadergui.kv which is
					  # class name without App, in lowercases

		# setting the app dimensions
		if os.name != 'posix':
			# running app om Windows
			Config.set('graphics', 'width', '600')
			Config.set('graphics', 'height', '500')
			Config.write()


if __name__ == '__main__':
	FileChooserEditorApp().run()
