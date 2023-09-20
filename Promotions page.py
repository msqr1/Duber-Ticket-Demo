from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup


class PromotionApp(App):
    def build(self):
        self.promotions = [
            {"name": "50% discount for next ticket", "Status": "Active", "Eligibility": "All customers", "Requirements": "Purchase 20 tickets"},
            {"name": "20% promo card for a week", "Status": "Expired", "Eligibility": "New customers only", "Requirements": "Purchase 15 tickets"},
            {"name": "40$ discounted tickets for 3 days", "Status": "Active", "Eligibility": "Existing customers", "Requirements": "Purchase 10 tickets"},
        ]

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Promotions', size_hint=(1, 0.1)))
        self.promotion_list = BoxLayout(orientation='vertical', spacing=50, size_hint=(1, 0.7))

        for promotion in self.promotions:
            promotion_button = Button(text=promotion['name'])
            promotion_button.bind(on_press=lambda btn, promotion=promotion: self.show_promotion_details(promotion))
            self.promotion_list.add_widget(promotion_button)

        layout.add_widget(self.promotion_list)
        layout.add_widget(Button(text='Exit', size_hint=(1, 0.1), on_press=self.stop))

        return layout

    def show_promotion_details(self, promotion):
        popup_content = BoxLayout(orientation='vertical', spacing=10)
        popup_content.add_widget(Label(text=f"Promotion Name: {promotion['name']}"))
        popup_content.add_widget(Label(text=f"Status: {promotion['Status']}"))
        popup_content.add_widget(Label(text=f"Eligibility: {promotion['Eligibility']}"))
        popup_content.add_widget(Label(text=f"Requirements: {promotion['Requirements']}"))

        popup = Popup(title='Promotion Details', content=popup_content, size_hint=(None, None), size=(400, 200))
        popup.open()


if __name__ == '__main__':
    PromotionApp().run()
