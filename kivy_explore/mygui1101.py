from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton
from kivy.uix.settings import SettingsWithTabbedPanel

class RequestListButton(ListItemButton):
    pass


class MyGUI1101(BoxLayout):
    requestInput = ObjectProperty()
    requestList = ObjectProperty()
    resultOutput = ObjectProperty()
    statusBar = ObjectProperty()
    showRequestList = False

    def __init__(self, **kwargs):
        super(MyGUI1101, self).__init__(**kwargs)

        self.histoListItemHeight = 15
        self.histoListMaxVisibleItems = 3
        self.maxHistoListHeight = self.histoListMaxVisibleItems * self.histoListItemHeight

        self.appSize = 'Full'
        self.defaultAppPosAndSize = 'Full'
        self.appSizeHalfProportion = 0.56
        self.applyAppPosAndSize()

    def applyAppPosAndSize(self):
        self.size_hint_y = 1
        self.pos_hint = {'x': 0, 'y': 0}

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

        if requestStr != '' and not requestStr in self.requestList.adapter.data:
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
            listView.scroll_to(0)

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
            self.replayAllButton.disabled = True
            self.requestList.height = '0dp'
        else:
            self.toggleHistoButton.disabled = False
            self.replayAllButton.disabled = False

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

    def enableRequestListItemButtons(self):
        self.deleteButton.disabled = False

    def disableRequestListItemButtons(self):
        self.deleteButton.disabled = True

    def replayAllRequests(self):
        # output blank line
        self.outputResult('')

        for request in self.requestList.adapter.data:
            self.outputResult(request)

        # self.resultOutput.do_cursor_movement('cursor_pgdown')
        self.refocusOnRequestInput()


class MyGUI1101App(App):
    settings_cls = SettingsWithTabbedPanel

    def build(self): # implicitely looks for a kv file of name mygui1101.kv which is
                     # class name without App, in lowercases

        return MyGUI1101()


    def on_pause(self):
        # Here you can save data if needed
        return True


    def on_resume(self):
        # Here you can check if any data needs replacing (usually nothing)

        pass


if __name__ == '__main__':
    dbApp = MyGUI1101App()

    dbApp.run()
