import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyHelloWGUI(BoxLayout):
    def sayHello(self):
        print('Hello !')

    def sayBye(self):
        print('Bye !')

class HelloWApp(App):
    pass

if __name__ == '__main__':
    HelloWApp().run()