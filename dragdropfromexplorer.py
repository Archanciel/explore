from kivy.app import App
from kivy.core.window import Window

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy import Config
Config.set('graphics', 'multisamples', '0')

class WindowFileDropExampleApp(App):
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return

    def _on_file_drop(self, window, file_path):
        print(file_path)
        return

if __name__ == '__main__':
    WindowFileDropExampleApp().run()
