from kivy.app import App
from kivy.uix.label import Label


class HaloApp(App):
    def build(self):
        return Label(text="Halo dari Kivy!")


HaloApp().run()
