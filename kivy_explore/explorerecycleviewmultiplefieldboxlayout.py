from kivy.app import App
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

# data
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior

items = [{'number': '510001', 'name': 'Big Pump', 'size': '1.50 L', 'in_stock': True},
		 {'number': '523001', 'name': 'Leonie Still very, very,very long, long name', 'size': '1.60 L', 'in_stock': False},
		 {'number': '641301', 'name': 'Apple Mix', 'size': '1.30 L', 'in_stock': True},
		 {'number': '681301', 'name': 'Orange Mix', 'size': '1.40 L', 'in_stock': True}
		]


class MultiFieldLine(RecycleDataViewBehavior, BoxLayout):
	''' class layout defined in kv file '''
	index = None
	selected = BooleanProperty(False)
	selectable = BooleanProperty(True)
	
	def refresh_view_attrs(self, rv, index, data):
		''' Catch and handle the view changes '''
		self.rv = rv
		self.appGUI = rv.appGUI
		self.index = index
		
		return super(MultiFieldLine, self).refresh_view_attrs(
			rv, index, data)
	
	def on_touch_down(self, touch):
		''' Add selection on touch down '''
		if super(MultiFieldLine, self).on_touch_down(touch):
			return True
		if self.collide_point(*touch.pos) and self.selectable:
			return self.parent.select_with_touch(self.index, touch)
	
	def apply_selection(self, rv, index, is_selected):
		# instance variable used in .kv file to change the selected item
		# color !
		self.selected = is_selected
  
		if is_selected:
			print(rv.data[index])


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
								 RecycleBoxLayout):
	''' Adds selection and focus behaviour to the view. '''
	
	# required to authorise unselecting a selected item
	touch_deselect_last = BooleanProperty(True)


class AppGUI(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.rv.data = [{'label_1': str(x['number']), 'label_2': str(x['name']), 'label_3': str(x['size']), 'checkbox_1': x['in_stock']} for x in items]


class ExploreRecycleViewMultipleFieldBoxLayoutApp(App):
	def build(self):
		return AppGUI()


if __name__ == '__main__':
	ExploreRecycleViewMultipleFieldBoxLayoutApp().run()