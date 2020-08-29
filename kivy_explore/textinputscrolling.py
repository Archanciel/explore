from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class TextInputScrolling(BoxLayout):
    textInput = ObjectProperty()
    scroller = ObjectProperty()
    textOutput = ObjectProperty()

    def submitRequest(self):
        self.textOutput.text = self.textInput.text

    def text_changed(self, *args):
        width_calc = self.scroller.width
        for line_label in self.textOutput._lines_labels:
            width_calc = max(width_calc, line_label.width + 20)   # add 20 to avoid automatically creating a new line
        self.textOutput.width = width_calc

    def clearAll(self):
        self.textInput.text = ''
        self.textOutput.text = ''


class TextInputScrollingApp(App):
    def build(self):
        Config.set('graphics', 'width', '200')
        Config.set('graphics', 'height', '60')
        Config.write()

        self.gui = TextInputScrolling()
        return self.gui

TextInputScrollingApp().run()
