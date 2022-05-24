from tkinter import *
import tkintermapview

class Map(Toplevel):
    def __init__(self, window, latitude, longitude, name):
        super().__init__(window)
        self.title='map_view'
        self.map_widget = tkintermapview.TkinterMapView(self, width=400, height=400, corner_radius=0)
        self.marker = self.map_widget.set_position(latitude, longitude, marker=True)
        self.marker.set_text(name)
        self.map_widget.pack()
        self.map_widget.set_zoom(15)