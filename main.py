"""Alarm Clock using Python and Kivy for
CS50 Final Project
Uses www.forecast.io for weather results
(h/t to TODO: Add python forcast wrapper details )"""

import time
from kivy.utils import escape_markup
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
#from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#from datetime import datetime
#from kivy.graphics import Color
from kivy.uix.popup import Popup
#from kivy.core.text.markup import MarkupLabel
#from kivy.core.text import LabelBase
from kivy.properties import StringProperty
import forecastio

api_key = "9ca514decbdf7d7055ba9de5228cfa77"
lat = 52.3782080
lng = -1.7578900

forecast = forecastio.load_forecast(api_key, lat, lng)

class alarm(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super(Alarm, self).__init__(**kwargs)
    #     self.btn1.bind(on_release=self.btn1_pressed)
    #     self.btn2.bind(on_release=self.btn2_pressed)
    #     self.btn4.bind(on_release=self.btn4_pressed)
    #
    # def btn1_pressed(self, obj):
    #     exit()
    #
    # def btn2_pressed(self, obj):
    #     content = BoxLayout(orientation='vertical')
    #     label = Label(
    #         text=('[color=#59c6ff] hello World [/color]'), markup=True)
    #     btn3 = Button(text='close me!', background_normal='',
    #                   background_color=(0.349, 0.776, 1.0, 1.0))
    #     content.add_widget(label)
    #     content.add_widget(btn3)
    #
    #     popup = Popup(content=content,
    #                   title='Herrow?',
    #                   size_hint=(None, None), size=(400, 400),
    #                   auto_dismiss=False,
    #                   background='',
    #                  )
    #     popup.open()
    #     btn3.bind(on_release=popup.dismiss)
    #
    # def btn4_pressed(self, obj):
    #     content = BoxLayout(orientation='vertical')
    #     hourly= forecast.currently()
    #     currentForecast = str(hourly.summary)
    #     ForecastLabel = Label(
    #         text=('[color=#59c6ff]' + currentForecast + '[/color]'), markup = True)
    #     btn5 = Button(text='close me!', background_normal='',
    #                   background_color=(0.349, 0.776, 1.0, 1.0))
    #     content.add_widget(ForecastLabel)
    #     content.add_widget(btn5)
    #
    #     p2 = Popup(content=content,
    #                title='Forecast for today',
    #                size_hint=(None, None), size=(400, 400),
    #                auto_dismiss=False,
    #                background='',
    #                title_color = (0.349, 0.776, 1.0, 1.0),
    #               )
    #     p2.open()
    #     btn5.bind(on_release=p2.dismiss)

class AlarmApp(App):
    time = StringProperty()

    def showTime(self, *args):
        self.time = str(time.strftime('%H:%M:%S'))

    def build(self):
        parent = Widget()
        Clock.schedule_interval(self.showTime, 1)
        alarmbtn = Button(text = "Alarm")
        #alarmbtn.bind(on_release = alarm())
        parent.add_widget(alarmbtn)
        #Window.borderless = True
        #Window.fullscreen = True
        Window.clearcolor = (1, 1, 1, 1)
        return parent

if __name__ == '__main__':
    AlarmApp().run()
