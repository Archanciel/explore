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
		 {'number': '523001', 'name': 'Leonie Still', 'size': '1.60 L', 'in_stock': False},
		 {'number': '641301', 'name': 'Apple Mix', 'size': '1.30 L', 'in_stock': True},
		 {'number': '681301', 'name': 'Orange Mix', 'size': '1.40 L', 'in_stock': True}
		]


class MultiFieldLine(RecycleDataViewBehavior, BoxLayout):
	# class layout defined in kv file
	pass

class AppGUI(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.rv.data = [{'label_1': str(x['number']), 'label_2': str(x['name']), 'label_3': str(x['size']), 'checkbox_1': x['in_stock']} for x in items]


class ExploreRecycleViewMultipleFieldApp(App):
	def build(self):
		return AppGUI()


if __name__ == '__main__':
	ExploreRecycleViewMultipleFieldApp().run()