# draw a random walk
# with colour changing each turn
# and a thicker pen width

from turtle import Turtle, Screen
from random import choice

t = Turtle()

colour = ["red", "orange", "yellow", "green",
          "blue", "indigo", "violet", "purple"]

direction = [0, 90, 180, 270]

t.shape("turtle")
t.color("black", "olive drab")


def random_walk(steps):
    for _ in range(steps):
        turn = choice(direction)
        t.speed(10)
        t.pensize(10)
        t.pencolor(choice(colour))
        t.forward(50)
        t.setheading(turn)


random_walk(100)

s = Screen()
s.exitonclick()
