# draw and rotate equilateral triangles for the visual stimulation

from math import cos, pi, sin

class triangle():
    # length from centre to point
    # rotation in [0, 1]
    def __init__(self, canvas, x, y, radius, rotation, colour='white'):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.radians = rotation * 2 * pi
        self.colour = colour

    def draw(self):
        r1 = self.radians
        r2 = self.radians + 2 * pi / 3
        r3 = self.radians + 4 * pi / 3
        self.canvas.create_polygon(self.x + self.radius * cos(r1), \
                self.y + self.radius * sin(r1), \
                self.x + self.radius * cos(r2), \
                self.y + self.radius * sin(r2), \
                self.x + self.radius * cos(r3), \
                self.y + self.radius * sin(r3), fill=self.colour)
    def rotate(self, amount):
        self.radians += amount * 2 * pi * (1 if self.radians > 0 else -1)

