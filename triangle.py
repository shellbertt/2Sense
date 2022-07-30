# draw and rotate equilateral triangles for the visual stimulation

from math import cos, pi, sin

class triangle():
    # length from centre to point
    # rotation in [0, 1]
    def __init__(self, canvas, x, y, length, rotation, colour='white'):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.length = length
        self.radians = rotation * 2 * pi
        self.colour = colour

    def draw(self):
        r1 = self.radians
        r2 = self.radians + 2 * pi / 3
        r3 = self.radians + 4 * pi / 3
        self.canvas.create_polygon(self.x + self.length * cos(r1), \
                self.y + self.length * sin(r1), \
                self.x + self.length * cos(r2), \
                self.y + self.length * sin(r2), \
                self.x + self.length * cos(r3), \
                self.y + self.length * sin(r3), fill=self.colour)
    def rotate(self, rotation):
        self.radians += rotation * 2 * pi

