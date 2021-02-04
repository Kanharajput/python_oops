from kivy.app import App
from kivy.uix.widget import Widget


class PongApp(App):
    def build(self):
        return PongGame()

class PongGame(Widget):
    pass


PongApp().run()