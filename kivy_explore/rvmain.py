from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

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
#        self.selected = not self.selected
        if not self.selected and not is_selected:
            print(index, 'simply return')
            return
        elif self.selected and not is_selected:
            print(index, 'handling deselection')
#            self.unselected = True
            self.selected = False
        else:
            # if self.unselected:
            #     self.unselected = False
            #     return
            self.selected = not self.selected
            print(index, 'handling selection')

class KivyListView(BoxLayout):
    def __init__(self, **kwargs):
        super(KivyListView, self).__init__(**kwargs)
        self.recycleV.data = [{'text': str(x)} for x in range(100)]

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]

class RVMainApp(App):
    def build(self):
        return KivyListView()


if __name__ == '__main__':
    RVMainApp().run()