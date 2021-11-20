#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import partial

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup


class TestApp(App):
    def build(self):
        return Button(on_press=partial(self.popup_display, "title", "bar "*80))

    def popup_display(self, title, message, widget):
        l = Label(text=message)
        l.bind(size=lambda s, w: s.setter('text_size')(s, w))

        popup = Popup(content=l, title=title, size_hint=(None, None), size=(300, 200), auto_dismiss=True)

        popup.open()

if __name__ == '__main__':
    TestApp().run()