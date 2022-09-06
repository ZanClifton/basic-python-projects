# draw shapes from triangle to decagon
# with the same origin point

from turtle import Turtle, Screen

t = Turtle()

t.shape("turtle")
t.color("black", "olive drab")


def draw_shape(times, angle, colour):
    for _ in range(times):
        t.pencolor(colour)
        t.forward(100)
        t.right(angle)


draw_shape(3, 120, "red")
draw_shape(4, 90, "orange")
draw_shape(5, 72, "yellow")
draw_shape(6, 60, "green")
draw_shape(7, 51.43, "blue")
draw_shape(8, 45, "indigo")
draw_shape(9, 40, "violet")
draw_shape(10, 36, "purple")


s = Screen()
s.exitonclick()
