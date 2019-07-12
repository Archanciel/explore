from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import Screen

lost = Builder.load_file('Demo.kv')

class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableButton, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableButton, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected

    def on_enter(self):
        #layout=Patient()
        layout = App.get_running_app().root
        layout.change_dynamic_Layout()



class victor(BoxLayout):
    pass
class Patient(Screen):
    manage_prescription: ObjectProperty(None)

    #Method to change the dynamic pagelayout

    def change_dynamic_Layout(self):
        layout = Factory.victor()
        self.manage_prescription.clear_widgets()
        self.manage_prescription.add_widget(layout)
        print ('pressed')


class DemoApp(App):
    title = 'Hospital Management System'
    def build(self):
        n= Patient()
        return n

if __name__ == "__main__":
    DemoApp().run()