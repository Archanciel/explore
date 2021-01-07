from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

class MyW(BoxLayout):
    pass
class AnchorLayoutExplApp(App):
    def build(self):
        return MyW()

if __name__ == '__main__':
    AnchorLayoutExplApp().run()