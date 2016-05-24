from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.config import Config

class Alarm(Widget):
    pass

class AlarmApp(App):
    def build(self):
        Window.borderless = True
        Window.fullscreen = True
        return Alarm()

if __name__ == '__main__':
    AlarmApp().run()
