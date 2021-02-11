from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class ScrollableMarkupLabel(BoxLayout):
    textInput = ObjectProperty()
    scroller = ObjectProperty()
    textOutput = ObjectProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.currentLineNb = -1

    def submitRequest(self):
        self.currentLineNb += 1
        
        if self.textOutput.text and self.textOutput.text != '':
            self.textOutput.text = self.textOutput.text + '\n' + self.formatText(self.textInput.text, self.currentLineNb % 3)
        else:
            self.textOutput.text = self.formatText(self.textInput.text, self.currentLineNb % 3)

        self.textInput.text = ''
        self.textInput.focus = True

    def formatText(self, rawTxt, formatNb):
        if formatNb == 0:
            return rawTxt
        elif formatNb == 1:
            return '[b]' + rawTxt + '[/b]'
        elif formatNb == 2:
            return '[i]' + rawTxt + '[/i]'

    def text_changed(self, *args):
        width_calc = self.scroller.width
        for line_label in self.textOutput._lines_labels:
            width_calc = max(width_calc, line_label.width + 20)   # add 20 to avoid automatically creating a new line
        self.textOutput.width = width_calc

    def clearAll(self):
        self.currentLineNb = -1
        self.textInput.text = ''
        self.textOutput.text = ''
        self.textInput.focus = True


class ScrollableLabelMarkupApp(App):
    def build(self):
        Config.set('graphics', 'width', '300')
        Config.set('graphics', 'height', '100')
        Config.write()

        self.gui = ScrollableMarkupLabel()
        return self.gui

ScrollableLabelMarkupApp().run()
