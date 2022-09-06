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

a.shape("turtle")
a.color("black", "olive drab")
a.speed(10)
a.pensize(10)

for _ in range(200):
    a.color(random_colour())
    a.forward(30)
    a.setheading(choice(direction))

s = t.Screen()
s.exitonclick()
