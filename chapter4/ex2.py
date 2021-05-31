import turtle
pony = turtle.Turtle()
pony.speed(100)

import math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    """Draws a petal using two arcs.
    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    """Draws a flower with n petals.
    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.fd(length)
    t.pd()



# draw a sequence of three flowers, as shown in the book.
move(pony, -100)
flower(pony, 7, 60.0, 60.0)

move(pony, 100)
flower(pony, 10, 40.0, 80.0)

move(pony, 100)
flower(pony, 20, 140.0, 20.0)

pony.hideturtle()


turtle.mainloop()