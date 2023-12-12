
from kivy.app import App
#importing BoxLayout class from Kivy's boxlayout module. BoxLayout is used for arranging widgets in a vertical or horizontal box.
from kivy.uix.boxlayout import BoxLayout

# importing Button class from Kivy's button module. This is used to create interactive button widgets in the app.
from kivy.uix.button import Button

#importing Label class from Kivy's label module. Label is used to display text.
from kivy.uix.label import Label

#importing TextInput class from Kivy's textinput module. TextInput is used for user input of text.
from kivy.uix.textinput import TextInput

#to get httpx requests and send em
import httpx

# to translate
import xmltodict

class MyDCRApp(App):
    def __init__(self):
        App.__init__(self)
        self.password = TextInput(hint_text="Enter password", password=True)
        self.username = TextInput(hint_text="Enter username")
        self.graph_id = 1702933
        self.layout_box = BoxLayout(orientation='vertical')

    def build(self):
        b = Button(text="Create New Instance")
        b.bind(on_press=self.b_press)
        self.b_outer = BoxLayout()
        b_inner = BoxLayout()
        b_inner.add_widget(self.username)
        b_inner.add_widget(self.password)
        self.b_outer.add_widget(b)
        self.b_outer.add_widget(b_inner)
        return self.b_outer

    def b_press(self, instance):
        self.create_instance()

    def create_instance(self):
        newsim_response = httpx.post(
            url="https://repository.dcrgraphs.net/api/graphs/" + str(self.graph_id) + "/sims",
            auth=(self.username.text, self.password.text))

        simulation_id = newsim_response.headers['simulationID']
        print("New simulation created with id:", simulation_id)

        next_activities_response = httpx.get(
            "https://repository.dcrgraphs.net/api/graphs/" + str(self.graph_id) +
            "/sims/" + simulation_id + "/events?filter=only-enabled",
            auth=(self.username.text, self.password.text))

        events_xml = next_activities_response.text
        events_xml_no_quotes = events_xml[1:len(events_xml) - 1]
        events_xml_clean = events_xml_no_quotes.replace('\\\"', "\"")

        events_json = xmltodict.parse(events_xml_clean)

        for e in events_json['events']['event']:
            self.layout_box.add_widget(Label(text=e['@label']))
            print(e['@label'])

        self.b_outer.add_widget(self.layout_box)


if __name__ == '__main__':
    MyDCRApp().run()