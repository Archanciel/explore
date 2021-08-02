from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class RootWidget(FloatLayout):
    pass


class Test_2App(App):
    title = "With Inheritance of BLMother"

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    Test_2App().run()