from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup

import webbrowser

class ScrollablePopup(Popup):
    contentBox = ObjectProperty()
    scrollView = ObjectProperty()

    def updateScrollablePopupContentScrollToBottom(self):
        content = "Hello World\n"
        self.contentBox.content.text = content * 50
        self.scrollView.scroll_y = 0 # force scrolling to bottom


    def updateScrollablePopupContentScrollToTop(self):
        content = "Hello World\n"
        self.contentBox.content.text = content * 50
        self.scrollView.scroll_y = 1 # force scrolling to top
        
    def initText(self, text):
        self.contentBox.content.text = text
    	

class ScrollPopup(BoxLayout):
    popup = None

    def openBrowser(self):
        url = "https://www.youtube.com/watch?v=ZKv6hpddWYc"
        #url = "https://youtube.com/playlist?list=PLzwWSJNcZTMRKdsBnVLvj-0P2GlKJi6Pd"
        webbrowser.open(url, new=1)       

class OpenBrowserApp(App):
    def build(self): # implicitely looks for a kv file of name kivylistview1111.kv which is
                     # class name without App, in lowercases

        Config.set('graphics', 'width', '400')
        Config.set('graphics', 'height', '500')
        Config.write()

        return ScrollPopup()

    def on_pause(self):
        # Here you can save data if needed
        return True

    def on_resume(self):
        # Here you can check if any data needs replacing (usually nothing)
        pass

if __name__ == '__main__':
    OpenBrowserApp().run()