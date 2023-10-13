from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

class HomePage(App):
    def build(self):
        self.info = [
            {"Get Started": "Location", "Maps": "Use your mobile location to activate Maps"},
            {"Get Started": "Transportation", "Available": "Choose your bus/train"},
            {"Get Started": "Driver", "Id": "More information about your driver"},
        ]
        self.maps = [
            {'Maps': "Use your mobile location to activate Maps"},
        ]
        self.trans = [
            {'Transportation': "Choose your bus/train"},
        ]
        self.driver = [
            {'Driver': "More information about your driver"},
        ]



        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Get Started!', size_hint=(1, 0.1)))
        self.info_list = BoxLayout(orientation='vertical', spacing=50, size_hint=(1, 0.7))



        for info in self.info:
            info_button = Button(text=info['Get Started'])
            info_button.bind(on_press=lambda btn, info=info: self.show_info_details(info))
            self.info_list.add_widget(info_button)

        layout.add_widget(self.info_list)

        return layout

    def show_maps_details(self, maps):
        popup_content = BoxLayout(orientation='vertical', spacing=10)
        popup_content.add_widget(Label(text=f"Get Started with: {maps['Maps']}"))
        popup = Popup(title='Get Started!', content=popup_content, size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_info_details(self, trans):
        popup_content = BoxLayout(orientation='vertical', spacing=10)
        popup_content.add_widget(Label(text=f"Get Started with: {trans['Transportation']}"))
        popup = Popup(title='Get Started!', content=popup_content, size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_info_details(self, driver):
        popup_content = BoxLayout(orientation='vertical', spacing=10)
        popup_content.add_widget(Label(text=f"Get Started with: {driver['Driver']}"))
        popup = Popup(title='Get Started!', content=popup_content, size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == '__main__':
    HomePage().run()
