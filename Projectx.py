from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window

from kivymd.uix.textfield import MDTextField

#class introButton(App):
    #def build(self):
        #return Button(text="Welcome to Union", pos = (300, 350), size_hint = (.25, .18))
    

#Builder.load_string(""" 

#<KivyButton>:
    #Button:
        #text: 'nel'
        #size_hint: 200, .550
        #Image:
            #source: 'Not done.jpg'
            #center_x: self.parent.center_x
            #center_y: self.parent.center_y


#    """)

#class KivyButton(App, BoxLayout):
    #def build(self):
        #return self
    
#KivyButton().run()

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
            id: user
            icon_left: "account-check"
            hint_text: "Username"
            foreground_color: 1, 0, 1, 1
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
        MDTextField:
            mode: 'round'
            id: password
            icon_left: "key-variant"
            hint_text: "Password"
            foreground_color: 1, 0, 1, 1
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
            password: True
        MDFillRoundFlatButton:
            text: "LOG IN"

'''

class LoginApp(MDApp):
    dialog = None #
    
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'Green'

        return Builder.load_string(KV)
    

    def login(self):
        if self.root.ids.user.text == 'admin' and self.root.ids.password.text == '123':
            if not self.dialog:
                self.dialog = MDDialog(
                    title = 'Login',
                    text = f"Bienvenido{self.root.ids.user.text}!",
                    buttons = [
                        MDFlatButton(
                            text = "Ok", text_color = self.theme_cls.accent_color,
                            on_release = self.close
                            ),
                    ],  
                )   
                self.dialog.open()
    def close(self):
         self.dialog.dismiss()

LoginApp().run()









