from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import *
from kivymd.uix.pickers import *
from kivymd.app import MDApp
from kivy.lang.builder import Builder
class nbook(MDScreen): #Regular ticket screen
    def savedate(self,a,b,c):
        self.ids.rdbutton.text = str(b)
    def savetime(self,a,b):
        self.ids.rtbutton.text = str(b)
    def pickdate(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.savedate)
        date_dialog.open()
    def picktime(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.savetime)
        time_dialog.open()
class rbook(MDScreen): #Recurring ticket screen
    def savedate(self,a,b,c):
        self.ids.rdbutton.text = str(b)
        print(self.get_root_window().ids)
    def savetime(self,a,b):
        self.ids.rtbutton.text = str(b)
    def pickdate(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.savedate)
        date_dialog.open()
    def picktime(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.savetime)
        time_dialog.open()
class nbook2(MDScreen): #Next regular ticket screen
    pass
class Duber(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Yellow"
        sm = ScreenManager()
        sm.add_widget(nbook(name="nbook"))
        sm.add_widget(rbook(name="rbook"))
        return sm
Builder.load_string("")
Duber().run()
