from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

Builder.load_file('kivyrecycleview.kv')
#Builder.load_string('''
# <SelectableLabel>:
#     # Draw a background to indicate selection
#     canvas.before:
#         Color:
#             rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
#         Rectangle:
#             pos: self.pos
#             size: self.size
# <RV>:
#     viewclass: 'SelectableLabel'
#     SelectableRecycleBoxLayout:
#         default_size: None, dp(56)
#         default_size_hint: 1, None
#         size_hint_y: None
#         height: self.minimum_height
#         orientation: 'vertical'
#         multiselect: True
#         touch_multiselect: True
# ''')


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

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


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


class RV(RecycleView, Screen):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]

    def change_dynamic_Layout(self):
        # layout = Factory.victor()
        # self.manage_prescription.clear_widgets()
        # self.manage_prescription.add_widget(layout)
        print ('pressed')

class TestApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    TestApp().run()