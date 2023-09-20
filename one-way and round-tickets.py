from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

# in this code you can click on one-way and round-trip buttons to 
# change windows wich have the different informaton needed
# also, when you click on the search for tickets button it print "clicked the button"

class TicketBookingApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()

        # Create the main screen
        main_screen = MainScreen(name='main')
        sm.add_widget(main_screen)

        # Create the one-way screen
        one_way_screen = OneWayScreen(name='one_way')
        sm.add_widget(one_way_screen)

        return sm

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Labels for departure and destination
        departure_label = Label(text="From where:")
        destination_label = Label(text="To where:")

        # Text input fields for departure and destination
        departure_input = TextInput(hint_text="Enter departure location", multiline=False)
        destination_input = TextInput(hint_text="Enter destination location", multiline=False)

        # Horizontal layout for one-way and round-trip buttons
        trip_type_layout = BoxLayout(orientation='horizontal', spacing=10)
        one_way_button = Button(text="One-Way")
        one_way_button.bind(on_release=self.switch_to_one_way_screen)
        round_trip_button = Button(text="Round-Trip")
        trip_type_layout.add_widget(one_way_button)
        trip_type_layout.add_widget(round_trip_button)

        # Labels for date and time selection
        departure_date_label = Label(text="Departure Date (YYYY-MM-DD, Hh:Mn):")
        return_date_label = Label(text="Return Date (YYYY-MM-DD, Hr:Mn):")

        # Text input fields for date and time selection
        departure_date_input = TextInput(hint_text="Enter departure date", multiline=False)
        return_date_input = TextInput(hint_text="Enter return date", multiline=False)

        # Label for the number of people
        num_people_label = Label(text="Number of People:")

        # Text input field for the number of people
        num_people_input = TextInput(hint_text="Enter number of people", input_type="number", multiline=False)

        # Button to search for tickets
        search_button = Button(text="Search for Tickets", background_normal='', background_color=(0.4, 1, 0.5, 0.7))
        search_button.bind(on_release=self.on_search_button_click)

        # Add widgets to the main screen
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(departure_label)
        layout.add_widget(departure_input)
        layout.add_widget(destination_label)
        layout.add_widget(destination_input)
        layout.add_widget(trip_type_layout)
        layout.add_widget(departure_date_label)
        layout.add_widget(departure_date_input)
        layout.add_widget(return_date_label)
        layout.add_widget(return_date_input)
        layout.add_widget(num_people_label)
        layout.add_widget(num_people_input)
        layout.add_widget(search_button)
        
        self.add_widget(layout)

    def switch_to_one_way_screen(self, instance):
        self.manager.current = 'one_way'
    
    def on_search_button_click(self, instance):
        print('clicked the button')


class OneWayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Labels for departure and destination
        departure_label = Label(text="From where:")
        destination_label = Label(text="To where:")

        # Text input fields for departure and destination
        departure_input = TextInput(hint_text="Enter departure location", multiline=False)
        destination_input = TextInput(hint_text="Enter destination location", multiline=False)

        # Horizontal layout for one-way and round-trip buttons
        trip_type_layout = BoxLayout(orientation='horizontal', spacing=10)
        one_way_button = Button(text="One-Way")
        round_trip_button = Button(text="Round-Trip")
        round_trip_button.bind(on_release=self.switch_to_main_screen)
        trip_type_layout.add_widget(one_way_button)
        trip_type_layout.add_widget(round_trip_button)

        # Labels for date and time selection
        departure_date_label = Label(text="Departure Date (YYYY-MM-DD, Hh:Mn):")

        # Text input fields for date and time selection
        departure_date_input = TextInput(hint_text="Enter departure date", multiline=False)

        # Label for the number of people
        num_people_label = Label(text="Number of People:")

        # Text input field for the number of people
        num_people_input = TextInput(hint_text="Enter number of people", input_type="number", multiline=False)

        # Button to search for tickets
        search_button = Button(text="Search for Tickets", background_normal='', background_color=(0.4, 1, 0.5, 0.7))
        search_button.bind(on_release=self.on_search_button_click)

        # Add widgets to the main screen
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(departure_label)
        layout.add_widget(departure_input)
        layout.add_widget(destination_label)
        layout.add_widget(destination_input)
        layout.add_widget(trip_type_layout)
        layout.add_widget(departure_date_label)
        layout.add_widget(departure_date_input)
        layout.add_widget(num_people_label)
        layout.add_widget(num_people_input)
        layout.add_widget(search_button)
        
        self.add_widget(layout)

    def switch_to_main_screen(self, instance):
        self.manager.current = 'main'
    
    def on_search_button_click(self, instance):
        print('clicked the button')


if __name__ == '__main__':
    TicketBookingApp().run()
