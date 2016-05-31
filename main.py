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
from kivy.uix.popup import Popup
from kivy.core.text.markup import MarkupLabel
from kivy.core.text import LabelBase
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
import time
import forecastio



class Alarm(BoxLayout):

    def __init__(self, **kwargs):
        super(Alarm, self).__init__(**kwargs)
        btn1 = ObjectProperty(None)
        self.btn1.bind(on_release = self.btn1_pressed)
        btn2= ObjectProperty(None)
        self.btn2.bind(on_release= self.btn2_pressed)
        #self.today= datetime.now()
        clock = ObjectProperty(None)
        btnt4 = ObjectProperty(None)
        self.btn4.bind(on_release = self.btn4_pressed)
    #     self.clock = Label(text = self.today.strftime('[color= (0.827, 0.827, 0.827, 1)]%H:%M[/color]'), markup = True, font_size = 70, )
    #     self.add_widget(self.clock)
    #     self.btn1 = Button(text = 'Exit', background_normal ='', background_color = (0.349, 0.776, 1.0, 1.0))
    #     self.btn1.bind(on_release = self.btn1_pressed)
    #     self.btn2 = Button (text = 'Click Me', background_normal ='', background_color = (0.349, 0.776, 1.0, 1.0))
    #     self.btn2.bind(on_release = self.btn2_pressed)
    #     self.add_widget(self.btn1)
    #     self.add_widget(self.btn2)
    #
    def btn1_pressed(self, obj):
        exit()
    #
    def btn2_pressed(self, obj):
        content = BoxLayout(orientation = 'vertical')
        label= Label(text = ('[color= #59c6ff] hello World [/color]'), markup = True)
        btn3 = Button(text = 'close me!', background_normal ='', background_color = (0.349, 0.776, 1.0, 1.0))
        content.add_widget(label)
        content.add_widget(btn3)

        p= Popup(content = content,
                 title = 'Herrow?',
                 size_hint = (None, None), size= (400,400),
                 auto_dismiss = False,
                 background = '',
                 )
        p.open()
        btn3.bind(on_release = p.dismiss)

    def btn4_pressed(self, obj):
        content= BoxLayout(orientation= 'vertical')
        ForecastLabel= Label(text = ('[color= #59c6ff] Forecast goes here [/color]'), markup = True)
        btn5 = Button(text = 'close me!', background_normal ='', background_color = (0.349, 0.776, 1.0, 1.0))
        content.add_widget(ForecastLabel)
        content.add_widget(btn5)

        p2= Popup(content = content,
                  title = 'Forecast for today',
                  size_hint = (None, None), size= (400,400),
                  auto_dismiss = False,
                  background = '',
                  )
        p2.open()
        btn5.bind(on_release = p2.dismiss)

class AlarmApp(App):
    time = StringProperty()
    def showTime(self, *args):
        self.time= str(time.strftime('%H:%M:%S'))
    def build(self):
        Clock.schedule_interval(self.showTime, 1)
        # layout = BoxLayout (orientation = 'vertical', spacing = 10)
        #self.alarm = Alarm()
        # today= datetime.now()
        #showTime = today.strftime("%H:%M")
        # clock = Label(text = today.strftime("%H:%M"), font_size = 70)
        # btn1 = Button(text = 'Exit', background_normal ='', background_color = (0.349, 0.776, 1.0, 1.0))
        # btn1.bind(on_release = self.btn1_pressed)
        # btn2 = Button (text = 'Click Me', background_normal ='', background_color = (0.349, 0.776, 1.0, 1.0))
        # btn2.bind(on_release = self.btn2_pressed)
        #layout.add_widget(self.alarm)
        # layout.add_widget(clock)
        # layout.add_widget(btn2)
        # layout.add_widget(btn1)
        #Window.borderless = True
        #Window.fullscreen = True
        Window.clearcolor = (1, 1, 1, 1)
        return Alarm()

    # def btn1_pressed(self, obj):
    #     exit()
    #
    # def btn2_pressed(self, obj):
    #     content = BoxLayout(orientation = 'vertical')
    #     content.add_widget(Label(text = 'hello World'))
    #     btn3 = Button(text = 'close me!', background_normal ='', background_color = (0.349, 0.776, 1.0, 1.0))
    #     content.add_widget(btn3)
    #
    #     p= Popup(content = content,
    #              title = 'Herrow?',
    #              size_hint = (None, None), size= (400,400),
    #              auto_dismiss = False)
    #     p.open()
    #     btn3.bind(on_release = p.dismiss)

if __name__ == '__main__':
    AlarmApp().run()
