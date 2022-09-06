# draw a square

from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("black", "olive drab")

for _ in range(4):
    t.forward(100)
    t.right(90)


s = Screen()
s.exitonclick()
