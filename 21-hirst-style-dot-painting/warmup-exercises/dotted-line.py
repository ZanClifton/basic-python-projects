# draw a dotted line

from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("black", "olive drab")

for _ in range(20):
    t.pencolor("indigo")
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


s = Screen()
s.exitonclick()
