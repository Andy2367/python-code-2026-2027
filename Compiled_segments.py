import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import sqlite3

'''
All parts of progect together in one place
Andrew Fraser Cowie
IA
'''

class MyGridLayout(GridLayout):

    def __init__(self, **kwargs): # initialise infanaite keywords
        super(MyGridLayout, self).__init__(**kwargs) # call the frid layout constructor

        # main layout
        self.cols = 1 # num cols is set to 1
        self.padding = 10
        self.spacing = 5

        #upper layout
        self.inner_grid = GridLayout()
        self.inner_grid.cols = 2 # upper grid has 2 cols
        self.inner_grid.padding = 0 #upper grid is same width as main grid
        self.inner_grid.spacing = 5 # space between upper grid widgets is set to 5
        '''
        # grid for events
        # if used widgets don't apear in gui and if cols is set to more than 1 it efects the entire layout not just the row that it should (still working on solution)
        self.inner_low = GridLayout()
        self.cols = 1
        self.padding = 0
        self.spacing = 5
        '''
        self.inner_grid.add_widget(Button(text = "Selected events"))
        self.inner_grid.add_widget(Button(text = "Filter"))

        self.add_widget(self.inner_grid)

        self.add_widget(Label(text = "event 1"))
        self.add_widget(Label(text = "event 2"))
        self.add_widget(Label(text = "event 3"))

        self.add_widget(Button(text = "Submit changes", font_size = 32))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()