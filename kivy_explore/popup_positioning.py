from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.clock import Clock
 
 
class PopupApp(App):
    def build(self):
        p = Popup(title='test',
                  size_hint=(.5, .5),
                  pos_hint={'right': .9, 'top': 0.9})
 
        Clock.schedule_once(p.open, 2)
        return Widget()
 
 
PopupApp().run()