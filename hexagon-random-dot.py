import turtle as t
import math as mt
import random as rnd

t.bgcolor("black")

rt3 = mt.sqrt(3)

# Function to create the equilateral triangle
def triangle():
    t.penup()
    t.setposition(-150/2, 150 * rt3 / 2)
    t.pendown()
    t.setposition(150/2, 150 * rt3 / 2)
    t.setposition(150, 0)
    t.setposition(150/2, -150 * rt3 / 2)
    t.setposition(-150/2, -150 * rt3 / 2)
    t.setposition(-150, 0)
    t.setposition(-150/2, 150 * rt3 / 2)

# Function to measure distance between two coordinates
def dist(d1x, d2x, d1y, d2y):
    Dx = (d1x - d2x)
    Dy = (d1y - d2y)
    s = Dx * Dx + Dy * Dy
    d = mt.sqrt(s)
    return d

# Function to calculate centroid of a triangle
def cent(ax, ay, bx, by, cx, cy):
    X = (ax + bx + cx) / 3
    Y = (ay + by + cy) / 3
    return X, Y

# Set up initial triangle and random dot selection
t.color("white")
triangle()

dy = -150 * rt3 / 2
dx = -150 / 2

t.penup()
t.setposition(dx, dy)
t.pendown()
t.circle(1)

col = ["orange", "red", "green", "yellow", "white", "brown", "grey", "purple", "pink"]

# Generate dots using centroid method
for i in range(5000):
    sid = rnd.randint(1, 6)
    t.color(col[i % 8])
    
    if sid == 1:
        dx, dy = cent(-150/2, 150 * rt3 / 2, 150/2, 150 * rt3 / 2, dx, dy)
    elif sid == 2:
        dx, dy = cent(150/2, 150 * rt3 / 2, 150, 0, dx, dy)
    elif sid == 3:
        dx, dy = cent(150, 0, 150/2, -150 * rt3 / 2, dx, dy)
    elif sid == 4:
        dx, dy = cent(150/2, -150 * rt3 / 2, -150/2, -150 * rt3 / 2, dx, dy)
    elif sid == 5:
        dx, dy = cent(-150/2, -150 * rt3 / 2, -150, 0, dx, dy)
    elif sid == 6:
        dx, dy = cent(-150, 0, -150/2, 150 * rt3 / 2, dx, dy)

    t.speed(200)
    t.penup()
    t.setposition(dx, dy)
    t.pendown()
    t.circle(1)

t.done()
