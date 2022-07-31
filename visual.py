# generate and rotate many triangles

import triangle
from tkinter import *
from random import randint, random

class controller():
    def __init__(self, window, period):
        self.window = window
        screenh = window.winfo_screenheight()
        screenw = window.winfo_screenwidth()
        self.canvas = Canvas(window, bg='black', height=screenh, width=screenw)
        self.canvas.pack()
        self.period = period
        # balance number of triangles with their size so everything fits reasonably
        self.count = 500
        self.radius = int((screenw * screenh // self.count) ** .5)
        self.horizontal_count = screenw // self.radius
        self.vertical_count = screenh // self.radius
        self.count = self.horizontal_count * self.vertical_count
        # assure a minimum size
        while self.radius < 40:
            self.count -= 10
            self.radius = screenw * screenh // self.count
            self.horizontal_count = screenw // self.radius
            self.vertical_count = screenh // self.radius
            self.count = self.horizontal_count * self.vertical_count
        self.triangles = [triangle.triangle(self.canvas, x * self.radius + randint(-10, 10) + self.radius // 2 , y * self.radius + randint(-10, 10) + self.radius // 2, (self.radius - 10) // 2, random() - .5) for y in range(self.vertical_count + 1) for x in range(self.horizontal_count + 1)]

    def iterate(self, on):
        if on:
            for t in self.triangles:
                t.draw()
            self.canvas.update()
            for t in self.triangles:
                t.rotate(self.period)
        self.canvas.delete('all')

