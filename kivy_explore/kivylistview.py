from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton # requires kivy 1.10 !!

# RecycleView related imports
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior


class RequestListButton(ListItemButton):
    pass

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
        if not self.selected and not is_selected:
            # case when adding a new list item
            print(index, 'simply return')
            return
        elif self.selected and not is_selected:
            # toggling from selected to unselected
            print(index, 'handling deselection')
            self.selected = False
            rv.parent.parent.recycleViewSelectItem(index, is_selected)
        else:
            # toggling from unselected to selected
            self.selected = not self.selected
            print(index, 'handling selection')
            rv.parent.parent.recycleViewSelectItem(index, is_selected)

class KivyListView(BoxLayout):
    requestInput = ObjectProperty()
    requestList = ObjectProperty()
    resultOutput = ObjectProperty()
    showRequestList = False
    currentSelIndex = -1

    def __init__(self, **kwargs):
        super(KivyListView, self).__init__(**kwargs)

        self.histoListItemHeight = 15
        self.histoListMaxVisibleItems = 4
        self.maxHistoListHeight = self.histoListMaxVisibleItems * self.histoListItemHeight

    def toggleRequestList(self):
        '''
        called by 'History' toggle button to toggle the display of the history
        request list.
        '''
        if self.showRequestList:
            self.requestList.size_hint_y = None
            self.requestList.height = '0dp'
            self.disableRequestListItemButtons()
            self.showRequestList = False
        else:
            listItemNumber = len(self.requestList.adapter.data)
            self.requestList.height = min(listItemNumber * self.histoListItemHeight, self.maxHistoListHeight)
            self.showRequestList = True
            self.resetListViewScrollToEnd()
            self.refocusOnRequestInput()

    def submitRequest(self):
        # Get the request from the TextInput
        requestStr = self.requestInput.text

        self.outputResult(requestStr)

        if requestStr != '':
            # Add the full request to the ListView if not already in
            self.requestList.adapter.data.extend([requestStr])

            # Reset the ListView
            self.resetListViewScrollToEnd()

        self.manageStateOfRequestListButtons()
        self.requestInput.text = ''

        self.refocusOnRequestInput()

    def resetListViewScrollToEnd(self):
        listView = self.requestList
        maxVisibleItemNumber = self.histoListMaxVisibleItems
        listLength = len(listView.adapter.data)

        if listLength > maxVisibleItemNumber:
            listView.scroll_to(listLength - maxVisibleItemNumber)
        else:
            if self.showRequestList:
                listItemNumber = len(self.requestList.adapter.data)
                self.requestList.height = min(listItemNumber * self.histoListItemHeight, self.maxHistoListHeight)

        listView._trigger_reset_populate()

    def manageStateOfRequestListButtons(self):
        '''
        Enable or disable history request list related controls according to
        the status of the list: filled with items or empty.
        :return:
        '''
        if len(self.requestList.adapter.data) == 0:
            # request list is empty
            self.toggleHistoButton.state = 'normal'
            self.toggleHistoButton.disabled = True
        else:
            self.toggleHistoButton.disabled = False

    def outputResult(self, resultStr):
        if len(self.resultOutput.text) == 0:
            self.resultOutput.text = resultStr
        else:
            self.resultOutput.text = self.resultOutput.text + '\n' + resultStr

    def refocusOnRequestInput(self):
        # defining a delay of 0.1 sec ensure the
        # refocus works in all situations. Leaving
        # it empty (== next frame) does not work
        # when pressing a button !
        Clock.schedule_once(self._refocusTextInput, 0.1)

    def _refocusTextInput(self, *args):
        '''
        This method is here to be used as callback by Clock and must not be called directly
        :param args:
        :return:
        '''
        self.requestInput.focus = True

    def deleteRequest(self, *args):
        # If a list item is selected
        if self.requestList.adapter.selection:
            # Get the text from the item selected
            selection = self.requestList.adapter.selection[0].text

            # Remove the matching item
            self.requestList.adapter.data.remove(selection)

            # Reset the ListView
            self.resetListViewScrollToEnd()

            self.requestInput.text = ''
            self.disableRequestListItemButtons()

        self.manageStateOfRequestListButtons()
        self.refocusOnRequestInput()

    def historyItemSelected(self, instance):
        requestStr = str(instance.text)

        # counter-intuitive, but test must be defined that way !
        if instance.is_selected:
            # disabling the 2 history request list item related buttons
            self.disableRequestListItemButtons()
        else:
            self.enableRequestListItemButtons()

        self.requestInput.text = requestStr
        self.refocusOnRequestInput()

    def recycleViewSelectItem(self, index, isSelected):
        if isSelected:
            self.currentSelIndex = index
            requestStr = self.requestListRV.data[index]['text']
            self.requestInput.text = requestStr
            self.enableRequestListItemButtons()
        else:
            self.currentSelIndex = -1
            self.requestInput.text = ''
            self.disableRequestListItemButtons()

    def enableRequestListItemButtons(self):
        self.deleteButton.disabled = False

    def disableRequestListItemButtons(self):
        self.deleteButton.disabled = True
        self.refocusOnRequestInput()

class KivyListViewApp(App):
    '''
    Requires Kivy1.10 to work since ListView is no longer available in newer versions of Kivy.
    '''

    def build(self): # implicitely looks for a kv file of name kivylistview.kv which is
                     # class name without App, in lowercases

        Config.set('graphics', 'width', '250')
        Config.set('graphics', 'height', '300')
        Config.write()

        return KivyListView()


    def on_pause(self):
        # Here you can save data if needed
        return True


    def on_resume(self):
        # Here you can check if any data needs replacing (usually nothing)
        pass

if __name__ == '__main__':
    dbApp = KivyListViewApp()

    dbApp.run()
