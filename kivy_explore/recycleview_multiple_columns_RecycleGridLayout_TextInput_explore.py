from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.textinput import TextInput

items = [{'SP1': 'Artikelnummer', 'SP2': 'Name', 'SP3': 'Groesse'},
         {'SP1': '510001', 'SP2': 'Big Pump', 'SP3': '1.50 L'},
         {'SP1': '523001', 'SP2': 'Leonie Still', 'SP3': '1.50 L'},
         {'SP1': '641301', 'SP2': 'Cola Mix', 'SP3': '1.50 L'}
         ]

class EditableTextInput(TextInput):
    def textChanged(self):
        print(self.text)

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': val} for row in items for val in row.values()]

class TestRVGridLayoutTextInputApp(App):
    def build(self):
        return RV()


if __name__ == '__main__':
    TestRVGridLayoutTextInputApp().run()