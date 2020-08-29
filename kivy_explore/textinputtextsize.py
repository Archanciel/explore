from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class TextInputTextSize(BoxLayout):
    textInput = ObjectProperty()
    textOutput = ObjectProperty()

    def submitRequest(self):
        # Get the request from the TextInput
        textInputTxt = self.textInput.text
        self.textOutput.text = textInputTxt
        textSize = self.textOutput._lines_labels[0].width
        print(textSize)

        if textSize > 392:
            self.textOutput.font_size -= 3
            self.textOutput.text = ''
            self.textOutput.text = textInputTxt
            textSize = self.textOutput._lines_labels[0].width
            print(textSize)

        self.textOutput.text = textInputTxt

    def outputTextChanged(self, text_input, text):
        if len(text) > 0:
            text_size = text_input._lines_labels[0].width
            print('font size: ', text_input.font_size, ' ', text, ': ', text_size)

class TextInputTextSizeApp(App):
    def build(self):
        return TextInputTextSize()

if __name__ == '__main__':
    TextInputTextSizeApp().run()
