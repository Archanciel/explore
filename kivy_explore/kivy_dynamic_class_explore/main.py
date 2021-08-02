from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class RootWidget(FloatLayout):
    pass


class TestApp(App):
    title = "With Inheritance of BLMother"

    def build(self):
        return RootWidget()


if __name__ == "__main__":
    TestApp().run()