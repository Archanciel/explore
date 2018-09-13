# ScatterDemo.py https://pythonmobile.blogspot.com/2014/07/42-scatter.html

from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App


class SquareWidget(Widget):
    pass


class ScatterWidget(Scatter):
    pass


class ScatterDemo(RelativeLayout):
    pass


class ScatterDemoApp(App):
    def build(self):
        return ScatterDemo()


if __name__ == '__main__':
    ScatterDemoApp().run()

