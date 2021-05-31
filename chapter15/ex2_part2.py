import math
import turtle


class Point:
    """Represents a Point."""


class Circle:
    """Represents a circle.
    
    attributes: center, radius
    """

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def draw_circle(t, c):
    angle = 360
    arc = 2 * math.pi * c.radius * angle / 360
    n = int(arc / 3) + 1
    step_length = arc / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

pony = turtle.Turtle()
pony.speed(100)



cir = Circle()
cir.center = Point()
cir.center.x = 150
cir.center.y = 100
cir.radius = 75

draw_circle(pony, cir)

turtle.mainloop()