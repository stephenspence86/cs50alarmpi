from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from datetime import datetime
from kivy.graphics import Color

class Alarm(Widget):
    pass

class AlarmApp(App):
    def build(self):
        layout = BoxLayout (orientation = 'vertical', spacing = 10)
        #self.alarm = Alarm()
        today= datetime.now()
        #showTime = today.strftime("%H:%M")
        clock = Label(text = today.strftime("%H:%M"), font_size = 70)
        btn1 = Button(text = 'Exit')
        btn1.bind(on_release = self.btn1_pressed)
        btn2 = Button (text = 'Change Color')
        btn2.bind(on_release = self.btn2_pressed)
        #layout.add_widget(self.alarm)
        layout.add_widget(clock)
        layout.add_widget(btn2)
        layout.add_widget(btn1)
        #Window.borderless = True
        #Window.fullscreen = True
        return layout

    def btn1_pressed(self, obj):
        exit()

    def btn2_pressed(self, obj):
        clock = Label(text = '[color = 59c6ff] today.strftime("%H:%M") [/color]', markup = True, font_size = 70, )

if __name__ == '__main__':
    AlarmApp().run()
