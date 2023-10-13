from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

from kivymd.uix.textfield import MDTextField

Window.size=(300,450)
KV='''
Screen:
    MDCard:
        size_hint: None, None
        size: 300, 450
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 65
        spacing: 35
        orientation: 'vertical'
        MDIcon:
            icon: 'account'
            icon_color: 0, 0, 0, 0
            haling: 'center'
            font_size: 180
        
        MDTextField:
            mode: 'round'
            id: user2
            icon_left: ""
            hint_text: "name of the user..."
            foreground_color: 1, 0, 1, 1
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
        MDTextField:
            mode: 'round'
            id: password
            icon_left: "key-variant"
            hint_text: "********"
            foreground_color: 1, 0, 1, 1
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
            password: True
        
        MDFillRoundFlatButton:
            text: "Change the Password"

'''

class ProfilePage(MDApp):
    dialog = None #
    
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'Green'

        return Builder.load_string(KV)
    

    def login(self):
        self.dialog.open()
    def close(self):
         self.dialog.dismiss()

ProfilePage().run()
