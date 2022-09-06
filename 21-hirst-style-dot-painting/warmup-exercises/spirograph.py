import turtle as t
from random import choice, randint

a = t.Turtle()
t.colormode(255)


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


direction = [0, 90, 180, 270]

a.shape("circle")
a.speed(20)
a.pensize(1)

for _ in range(90):
    a.color(random_colour())
    a.circle(100)
    a.right(4)

s = t.Screen()
s.exitonclick()
