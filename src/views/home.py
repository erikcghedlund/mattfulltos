from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivy.core.window import Window

Window.size = (450, 800)


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        grid = MDGridLayout(adaptive_size=True, size_hint=(1, 0.7))
        grid.cols = 2
        grid.rows = 3
        for s in ["Öl", "Cider", "Vin", "Sprit", "Drink", "Samma igen"]:
            grid.add_widget(
                MDRoundFlatButton(
                    text=s,
                    size_hint=(1, 1),
                ),
            )
        #screen.add_widget(grid)
        return grid


MainApp().run()
