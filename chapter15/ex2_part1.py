import math
import turtle


class Point:
    """Represents a Point."""


class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """


def draw_rect(t, rect):
    for i in range(2):
        t.fd(rect.width)
        t.rt(90)
        t.fd(rect.height)
        t.rt(90)

pony = turtle.Turtle()
pony.speed(100)

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

draw_rect(pony, box)

turtle.mainloop()