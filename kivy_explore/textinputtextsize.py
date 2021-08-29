from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout


class TextInputTextSize(BoxLayout):
    textInput = ObjectProperty()
    textInputMultiline = ObjectProperty()

    def submitRequest(self):
        # Get the request from the TextInput
        textInputTxt = self.textInputSingleLine.text
        self.textInputMultiline.text += '\n' + textInputTxt

    def printTextInputValue(self):
        print(self.textInputMultiline.text)
        
class TextInputTextSizeApp(App):
    def build(self):
        return TextInputTextSize()

if __name__ == '__main__':
    TextInputTextSizeApp().run()
