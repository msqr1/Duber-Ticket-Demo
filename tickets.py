from kivymd.uix.screenmanager import ScreenManager
from kivymd.theming import ThemeManager
from kivymd.uix.screen import *
from kivymd.uix.pickers import *
from kivymd.app import MDApp
import datetime
usrconfig = {
            'st': None, #start location
            'sd': [], #start date, repetition amount (0 for regular ticket)
            'sl': None, #start time
            'dst': None, #destination
            'ppl': None #people amount
        }
class book1:
    def savedate(self,a,b,c):        
        self.ids.rdbutton.text = str(b)
    def savetime(self,a,b):
        global usrconfig
        self.ids.rtbutton.text = str(b)
        usrconfig['st'] = b
    def pickdate(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.savedate)
        date_dialog.open()
    def picktime(self):
        time_dialog = MDTimePicker(
            primary_color="black",
            text_color="black"
        )
        if(usrconfig['st']):
            time_dialog.set_time(usrconfig['st'] if usrconfig['st'].hour != 0 else datetime.time.fromisoformat("12:00:00"))
        time_dialog.bind(on_save=self.savetime)
        time_dialog.open()
class book2:
    pass
class nbook(MDScreen,book1): #Regular ticket screen 
    pass
class rbook(MDScreen,book1): #Recurring ticket screen
    def savedate(self,a,b,c):
        print(b,c)
        self.ids.rdbutton.text = str(str(b).replace("-","/") + "  -  " + str(c[len(c)-1]).replace("-","/"))
    def pickdate(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.savedate)
        date_dialog.open()
class nbook2(MDScreen,book2): #Next regular ticket screen
    pass
class rbook2(MDScreen,book2): #Next recurring ticket screen
    pass
class Duber(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" #Dark theme
        self.theme_cls.primary_palette = "Green"  #Green accent
        sm = ScreenManager()
        sm.add_widget(nbook(name="nbook"))
        sm.add_widget(rbook(name="rbook"))
        return sm
Duber().run()
