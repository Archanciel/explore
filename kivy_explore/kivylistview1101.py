from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton # requires kivy 1.10 !!
from kivy.uix.settings import SettingsWithTabbedPanel
from kivy.config import Config


class RequestListButton(ListItemButton):
    pass


class KivyListView1101(BoxLayout):
    requestInput = ObjectProperty()
    requestList = ObjectProperty()
    resultOutput = ObjectProperty()
    showRequestList = False

    def __init__(self, **kwargs):
        super(KivyListView1101, self).__init__(**kwargs)

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

    def historyItemSelected(self, instance):
        requestStr = str(instance.text)
        self.requestInput.text = requestStr
        self.refocusOnRequestInput()


class KivyListView1101App(App):
    settings_cls = SettingsWithTabbedPanel

    def build(self): # implicitely looks for a kv file of name kivylistview1101.kv which is
                     # class name without App, in lowercases

        Config.set('graphics', 'width', '300')
        Config.set('graphics', 'height', '500')
        Config.write()

        return KivyListView1101()


    def on_pause(self):
        # Here you can save data if needed
        return True


    def on_resume(self):
        # Here you can check if any data needs replacing (usually nothing)

        pass


if __name__ == '__main__':
    dbApp = KivyListView1101App()

    dbApp.run()
