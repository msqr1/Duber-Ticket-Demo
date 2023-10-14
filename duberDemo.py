from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import *
from kivymd.uix.pickers import *
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import *
from kivy.uix.popup import Popup
import datetime
import time
#rider's request
usrConfig = {
    'st': None, #start time
    'sd': [], #start date, repetition amount (0 for regular ticket)
    'sl': None, #start location
    'dst': None, #destination
    'ppl': None, #people amount
}
state = { 
    'lastTicketPage': None 
}
#User's profile
class usrProfile(MDScreen):
    def switchScreen(self,screen=None):
        print(state['lastTicketPage'])
        if(state['lastTicketPage'] is not None):
            self.manager.current = state["lastTicketPage"]

#Promotion screen
class promo(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(super, **kwargs)
        layout = MDBoxLayout(orientation='vertical')
        self.promotions = [
            {"name": "50% discount for next ticket", "Status": "Active", "Eligibility": "All customers", "Requirements": "Purchase 20 tickets"},
            {"name": "20% promo card for a week", "Status": "Expired", "Eligibility": "New customers only", "Requirements": "Purchase 15 tickets"},
            {"name": "40$ discounted tickets for 3 days", "Status": "Active", "Eligibility": "Existing customers", "Requirements": "Purchase 10 tickets"},
            {"name": "30% discount for next ticket", "Status": "Requirements not met", "Eligibility": "All customers", "Requirements": "Purchase 13 tickets"},
        ]
        layout = MDBoxLayout(orientation='vertical')
        title = MDBoxLayout(orientation='vertical')
        label = MDLabel(text='Promotions',halign='center',valign='center')
        label.font_size='30sp'
        label.size_hint_y='0.25'
        title.add_widget(label)
        layout.add_widget(title)
        for promotion in self.promotions:
            ilayout = MDBoxLayout(orientation='vertical')
            promotion_button = MDRaisedButton(text=promotion['name'],font_size='20sp')
            promotion_button.size_hint_x=1
            promotion_button.padding='20sp'
            promotion_button.bind(on_release=lambda a,promotion=promotion:self.show_promotion_details(promotion))
            ilayout.add_widget(promotion_button)
            layout.add_widget(ilayout)
        buttons = MDBoxLayout(orientation='horizontal')
        button = MDIconButton(icon="ticket-outline",on_release=self.switchScreen)
        button.size_hint_x = 0.33
        buttons.add_widget(button)
        button = MDIconButton(icon="ticket-percent")
        button.size_hint_x = 0.33
        buttons.add_widget(button)
        button = MDIconButton(icon="account-outline",on_release=self.accountScreen)
        button.size_hint_x = 0.33
        buttons.add_widget(button)
        layout.add_widget(buttons)
        self.add_widget(layout)
    def accountScreen(self,screen=None):
        self.manager.current = "usrProfile"
    def switchScreen(self,screen=None):
        if(state['lastTicketPage'] is not None):
            self.manager.current = state["lastTicketPage"]
    def show_promotion_details(self, promotion):
        popup_content = MDBoxLayout(orientation='vertical', spacing=10)
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
        state['lastTicketPage'] = "nbook1"
    def switchTicketType(self, screen): #Carry the data between screen
        if(screen.name == "nbook1" or screen.name == "rbook1"):
            if(usrConfig['st'] is not None):
                self.ids.st.text = str(usrConfig['st'])
            if(usrConfig['sl'] is not None):
                self.ids.sl.text = usrConfig['sl']
            if(usrConfig['dst'] is not None):
                self.ids.dst.text = usrConfig['dst']
            if(usrConfig['ppl'] is not None):
                self.ids.ppl.text = usrConfig['ppl']
            state['lastTicketPage'] = screen.name
    def switchScreen(self,screen=None):
        print(state['lastTicketPage'])
        if(state['lastTicketPage'] is not None):
            self.manager.current = state["lastTicketPage"]
    def proceed(self):
        print("Coming Soon!")
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
        sm.add_widget(usrProfile(name="usrProfile"))
        return sm
duberDemo().run()
