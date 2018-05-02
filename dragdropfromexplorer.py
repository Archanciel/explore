from kivy.app import App
from kivy.core.window import Window
'''
Requires pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew as additional 
dependancies
'''

class WindowFileDropExampleApp(App):
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return

    def _on_file_drop(self, window, file_path):
        print(file_path)
        return

if __name__ == '__main__':
    WindowFileDropExampleApp().run()
