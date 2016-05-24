from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock

import time

class Alarm(Widget):
    pass

#class clock(Label):
#    def update(self, *args):
#        self.time = time.asctime()

class AlarmApp(App):
    def build(self):
        #clockLabel = clock()
        #Clock.schedule_interval(clockLabel.update, 1)
        Window.borderless = True
        #Window.fullscreen = True
        return Alarm()

if __name__ == '__main__':
    AlarmApp().run()
