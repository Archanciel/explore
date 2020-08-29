from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text='Move me !',
                  font_size=15)

        f.add_widget(s)
        s.add_widget(l)
        return f
        
if __name__ == "__main__":
    t = TutorialApp()
    t.run()