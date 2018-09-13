# DragDemo.py

from kivy.uix.widget import Widget
from kivy.uix.behaviors import DragBehavior
from kivy.app import App
from kivy.properties import StringProperty


class Horse(DragBehavior, Widget):
    horse_state = StringProperty('Not Dragging')

    def on_touch_move(self, touch):
        tx, ty = touch.pos
        sx, sy = self.pos
        if sx + 52 >= tx > sx + 36 and sy + 53 >= ty > sy + 28:
            self.horse_state = 'Dragging'

        #drag_rectangle in kv file specify the zone in the horse image where dragging is active !
        return super(Horse, self).on_touch_move(touch)


class DragDemo(Widget):
    pass


class DragDemoApp(App):
    def build(self):
        return DragDemo()


if __name__ == '__main__':
    DragDemoApp().run()