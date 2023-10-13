from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import *
from kivymd.uix.pickers import *
from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivy.uix.popup import Popup
import datetime
import random
#rider's request
usrConfig = {
            'st': None, #start time
            'sd': [], #start date, repetition amount (0 for regular ticket)
            'sl': None, #start location
            'dst': None, #destination
            'ppl': None, #people amount
        }
state = { 
    'lastTicketPage': None #last ticket page, 0 for regular, 1 for recurring
}
class promo(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(super, **kwargs)
        self.promotions = [
            {"name": "50% discount for next ticket", "Status": "Active", "Eligibility": "All customers", "Requirements": "Purchase 20 tickets"},
            {"name": "20% promo card for a week", "Status": "Expired", "Eligibility": "New customers only", "Requirements": "Purchase 15 tickets"},
            {"name": "40$ discounted tickets for 3 days", "Status": "Active", "Eligibility": "Existing customers", "Requirements": "Purchase 10 tickets"},
        ]
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(MDLabel(halign="center", text='Promotions', font_size='30sp', size_hint=(1,.1)))
        self.promotion_list = BoxLayout(orientation='vertical', spacing=50, size_hint=(1, 0.7))
        for promotion in self.promotions:
            promotion_Button = MDRaisedButton(halign="center", text=promotion['name'],size_hint=(1,.3))
            promotion_Button.bind(on_release=lambda btn, promotion=promotion: self.show_promotion_details(promotion))
            self.promotion_list.add_widget(promotion_Button)

        layout.add_widget(self.promotion_list)
        self.add_widget(layout)
    
    def show_promotion_details(self, promotion):
        popup_content = BoxLayout(orientation='vertical', spacing=10)
        popup_content.add_widget(MDLabel(text=f"Promotion Name: {promotion['name']}"))
        popup_content.add_widget(MDLabel(text=f"Status: {promotion['Status']}"))
        popup_content.add_widget(MDLabel(text=f"Eligibility: {promotion['Eligibility']}"))
        popup_content.add_widget(MDLabel(text=f"Requirements: {promotion['Requirements']}"))

        popup = Popup(title='Promotion Details', content=popup_content, size_hint=(None, None), size=(400, 200))
        popup.open()
    

#Base class for both regular and recurring ticket screen
class book1(MDScreen):
    def __init__(self, **kwargs): #initialize and bind screen (ticket type) switching event
        super().__init__(super, **kwargs)
        super().bind(on_pre_enter=self.switchTicketType)
    def switchTicketType(self, screen): #Carry the data between screen
        if(screen == "nbook1" or screen == "rbook1"):
            if(usrConfig['st'] is not None):
                self.ids.st.text = str(usrConfig['st'])
            if(usrConfig['sl'] is not None):
                self.ids.sl.text = usrConfig['sl']
            if(usrConfig['dst'] is not None):
                self.ids.dst.text = usrConfig['dst']
            if(usrConfig['ppl'] is not None):
                self.ids.ppl.text = usrConfig['ppl']
    def proceed(self):
        print("Coming Soon!")
    def switchScreen(self):
        if(state['lastTicketPage'] is not None):
            self.manager.current = "nbook1" if state['lastTicketPage'] == 0 else "rbook1"
    def recordInputs(self,text,att): #Record inputs for text fields into usrConfig
        usrConfig[att] = text
    def saveDate(self,a,b,c):  #Save the selected date into usrConfig
        self.ids.sd.text = str(b).replace("-","/")
        usrConfig['sd'] = [b,0]
    def saveTime(self,a,b): #Save the time into usrConfig
        self.ids.st.text = str(b)
        usrConfig['st'] = b
    def pickDate(self): #Open the datePicker menu
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.saveDate)
        date_dialog.open()
    def pickTime(self): #Open the timePicker menu, fixing some color
        time_dialog = MDTimePicker(
            primary_color="black",
            text_color="black"
        )
        if(usrConfig['st']): #Load the saved time so users don't need to re-enter
            time_dialog.set_time(usrConfig['st'] if usrConfig['st'].hour != 0 else datetime.time.fromisoformat("12:00:00"))
        time_dialog.bind(on_save=self.saveTime)
        time_dialog.open()

#Base class for direct/intergration general information screen

#Specific implementation of each screen from book1 
class nbook1(book1): #Regular ticket screen 
    pass
class rbook1(book1): #Recurring ticket screen
    #Overriding some methods for recurring tickets...
    def saveDate(self,a,b,c): #Save the ranged date into usrConfig 
        b = c[0]
        c = c[len(c)-1]
        self.ids.sd.text = str(str(b).replace("-","/") + "  -  " + str(c).replace("-","/"))
        usrConfig['sd'] = b,(c-b).days
    def pickDate(self): #Open the ranged datePicker
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.saveDate)
        date_dialog.open()

class duberDemo(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green" 
        sm = ScreenManager()
        sm.add_widget(nbook1(name="nbook1"))
        sm.add_widget(rbook1(name="rbook1"))
        sm.add_widget(promo(name="promo"))
        return sm
duberDemo().run()
