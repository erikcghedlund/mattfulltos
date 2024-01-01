from kivy.uix.screenmanager import Screen
import matplotlib.pyplot as plt
from kivymd.app import MDApp
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

Window.size = (450, 800)
plt.plot([1, 23, 2, 4])
plt.ylabel('some numbers')

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        box = BoxLayout(orientation="vertical", pos_hint={"y": 0.1})
        grid = MDGridLayout(adaptive_size=True, size_hint=(0.7, 0.5), pos_hint={"center_x": 0.5})
        grid.cols = 2
        grid.rows = 3
        for s in ["Öl", "Cider", "Vin", "Sprit", "Drink", "Samma igen"]:
            grid.add_widget(
                MDRoundFlatButton(
                    text=s,
                    font_size=20,
                    size_hint=(1, 1),
                ),
            )
        #screen.add_widget(grid)
        img = Image(source="./tmp.png", fit_mode="contain")
        #box.add_widget(img)
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        box.add_widget(grid)
        return box


MainApp().run()
