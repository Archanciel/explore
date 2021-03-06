import os
from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# RecycleView related imports
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior


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
            rv.parent.parent.recycleViewCurrentSelIndex = index

class KivyRecycleView(BoxLayout):
    requestInput = ObjectProperty()
    resultOutput = ObjectProperty()
    showRequestList = False
    currentSelIndex = -1
    recycleViewCurrentSelIndex = -1

    def __init__(self, **kwargs):
        super(KivyRecycleView, self).__init__(**kwargs)
        
        if os.name == 'posix':
            self.histoListItemHeight = 35
        else:
            self.histoListItemHeight = 15  
        	      	
        self.histoListMaxVisibleItems = 4
        self.maxHistoListHeight = self.histoListMaxVisibleItems * self.histoListItemHeight
        # setting RecycleView list item height from config
        self.requestListRVSelBoxLayout.default_size = None, self.histoListItemHeight
        self.requestListRVSelBoxLayout.spacing = 0.5

    def toggleRequestList(self):
        '''
        called by 'History' toggle button to toggle the display of the history
        request list.
        '''
        if self.showRequestList:
            # hiding RecycleView list
            self.boxLayoutContainingRV.height = '0dp'

            self.disableRequestListItemButtons()
            self.showRequestList = False
        else:
            # showing RecycleView list
            self.showRequestList = True
            self.adjustRequestListSize()
            self.resetListViewScrollToEnd()
            self.refocusOnRequestInput()

    def adjustRequestListSize(self):
        listItemNumber = len(self.requestListRV.data)
        self.boxLayoutContainingRV.height = min(listItemNumber * self.histoListItemHeight, self.maxHistoListHeight)
        return listItemNumber

    def resetListViewScrollToEnd(self):
        maxVisibleItemNumber = self.histoListMaxVisibleItems
        listLength = len(self.requestListRV.data)

        if listLength > maxVisibleItemNumber:
            # for the moment, I do not know how to scroll to end of RecyclweView !
            # listView.scroll_to(listLength - maxVisibleItemNumber)
            pass
        else:
            if self.showRequestList:
                listItemNumber = self.adjustRequestListSize()
                if listItemNumber == 0:
                    self.showRequestList = False
                    self.manageStateOfRequestListButtons()

    def submitRequest(self):
        # Get the request from the TextInput
        requestStr = self.requestInput.text

        self.outputResult(requestStr)

        if requestStr != '':
            # Add the full request to the RecycleView list
            listEntry = {'text': requestStr}

            if listEntry in self.requestListRV.data:
                print(requestStr, ' already in list will be removed !')
                self.requestListRV.data.remove(listEntry)

            self.requestListRV.data.append(listEntry)

            if self.showRequestList:
                self.adjustRequestListSize()

        self.manageStateOfRequestListButtons()
        self.requestInput.text = ''

        self.refocusOnRequestInput()

    def manageStateOfRequestListButtons(self):
        '''
        Enable or disable history request list related controls according to
        the status of the list: filled with items or empty.
        :return:
        '''
        if len(self.requestListRV.data) == 0:
            # request list is empty
            self.toggleHistoButton.state = 'normal'
            self.toggleHistoButton.disabled = True
            self.boxLayoutContainingRV.height = '0dp'
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
        # deleting from RecycleView list
        self.requestListRV.data.pop(self.currentSelIndex)
        self.requestListRV._get_layout_manager().clear_selection()

        if len(self.requestListRV.data) == 0:
            self.disableRequestListItemButtons()
            self.toggleHistoButton.disabled = True
            self.requestInput.text = ''

        if self.showRequestList:
            self.adjustRequestListSize()

        self.manageStateOfRequestListButtons()
        self.refocusOnRequestInput()

    def moveUpRequest(self):
        oldIndex = self.recycleViewCurrentSelIndex
        newIndex = oldIndex - 1
        requestTotalNumber = len(self.requestListRV.data)

        if newIndex < 0:
            # if first line request is moved up, it is moved at the end of the
            # request history list
            newIndex = requestTotalNumber - 1

        self.moveItemInList(list=self.requestListRV.data, oldIndex=oldIndex, newIndex=newIndex)

        if self.showRequestList:
            self.adjustRequestListSize()

        self.manageStateOfRequestListButtons()

    def moveDownRequest(self):
        oldIndex = self.recycleViewCurrentSelIndex
        newIndex = oldIndex + 1
        requestTotalNumber = len(self.requestListRV.data)

        if newIndex == requestTotalNumber:
            # if first line request is moved up, it is moved at the end of the
            # request history list
            newIndex = 0

        self.moveItemInList(list=self.requestListRV.data, oldIndex=oldIndex, newIndex=newIndex)

        if self.showRequestList:
            self.adjustRequestListSize()

        self.manageStateOfRequestListButtons()

    def moveItemInList(self, list, oldIndex, newIndex):
        list.insert(newIndex, list.pop(oldIndex))

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
        self.moveUpButton.disabled = False
        self.moveDownButton.disabled = False

    def disableRequestListItemButtons(self):
        self.deleteButton.disabled = True
        self.moveUpButton.disabled = True
        self.moveDownButton.disabled = True
        self.refocusOnRequestInput()

class KivyRecycleViewApp(App):
    def build(self): # implicitely looks for a kv file of name kivyrecycleview.kv which is
                     # class name without App, in lowercases

        Config.set('graphics', 'width', '250')
        Config.set('graphics', 'height', '300')
        Config.write()

        return KivyRecycleView()


    def on_pause(self):
        # Here you can save data if needed
        return True


    def on_resume(self):
        # Here you can check if any data needs replacing (usually nothing)
        pass

if __name__ == '__main__':
    dbApp = KivyRecycleViewApp()

    dbApp.run()
