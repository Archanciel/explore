from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior

items = [{'SP1': 'Artikelnummer', 'SP2': 'Name', 'SP3': 'Groesse'},
         {'SP1': '510001', 'SP2': 'Big Pump', 'SP3': '1.50 L'},
         {'SP1': '523001', 'SP2': 'Leonie Still', 'SP3': '1.50 L'},
         {'SP1': '641301', 'SP2': 'Cola Mix', 'SP3': '1.50 L'}
         ]

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        #self.data = [{'spalte1_SP': str(x['SP1']), 'spalte2_SP': str(x['SP2']), 'spalte3_SP': str(x['SP3'])} for x in items]
        self.data = [{'text': val} for row in items for val in row.values()]

class TestRVGridLayoutApp(App):
    def build(self):
        return RV()


if __name__ == '__main__':
    TestRVGridLayoutApp().run()