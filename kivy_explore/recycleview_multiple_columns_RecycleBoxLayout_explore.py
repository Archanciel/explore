from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView

items = [{'SP1': 'Artikelnummer', 'SP2': 'Name', 'SP3': 'Groesse'},
         {'SP1': '510001', 'SP2': 'Big Pump', 'SP3': '1.50 L'},
         {'SP1': '523001', 'SP2': 'Leonie Still', 'SP3': '1.50 L'},
         {'SP1': '641301', 'SP2': 'Cola Mix', 'SP3': '1.50 L'}
         ]


class Tabelle(BoxLayout):
    pass


class RV(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = [{'spalte1_SP': str(x['SP1']), 'spalte2_SP': str(x['SP2']), 'spalte3_SP': str(x['SP3'])} for x in items]

class TestRVBoxLayoutApp(App):
    def build(self):
        return RV()


if __name__ == '__main__':
    TestRVBoxLayoutApp().run()