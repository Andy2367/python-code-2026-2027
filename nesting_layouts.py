import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

        self.cols = 1

        self.inner = GridLayout()
        self.inner.cols = 2

        self.selected = (Button(text = "selected events"))
        self.inner.add_widget(self.selected)
        self.filter = (Button(text = "filter"))
        self.inner.add_widget(self.filter)
        self.add_widget(self.inner)
        self.add_widget(Label(text = "events"))

class MyApp(App):
    def Build(self):
        return MyLayout()

if __name__ == "__main__":
    MyApp().run()