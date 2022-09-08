from turtle import Turtle, Screen, color
from random import randint


def celebrate(turtle):
    turtle.right(180)
    turtle.forward(250)
    turtle.right(180)
    turtle.pencolor("black")
    turtle.write("I won!", font=('Arial', 20))
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(35)
    turtle.speed(5)
    turtle.circle(50)
    turtle.left(810)
    turtle.forward(75)
    turtle.left(180)


t = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=650, height=500)
screen.title("Turtle Race")
racing = False

t.penup()
t.hideturtle()
t.pencolor("pale green")
t.pensize(50)
t.speed(500)

for i in range(0, 6):
    t.goto(x=-375, y=100 - 40 * i)
    t.pendown()
    t.forward(750)
    t.penup()

t.pencolor("black")
t.pensize(1)

for i in range(1, 11):
    t.goto(x=-275 + 50 * i, y=150)
    t.write(i)
    t.setheading(-90)
    t.pendown()
    t.forward(300)
    t.penup()

t.home()
t.showturtle()

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

boxes = []

for box_index in range(0, 6):
    new_box = Turtle(shape="square")
    new_box.hideturtle()
    new_box.penup()
    new_box.color(colours[box_index])
    new_box.goto(x=-265, y=100 - 40 * box_index)
    new_box.showturtle()

bet = screen.textinput(title="Bet now!",
                       prompt="Which turtle do you think will win? Pick a colour: ").lower()

turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-265, y=100 - 40 * turtle_index)
    turtles.append(new_turtle)

if bet:
    t.hideturtle()
    t.goto(x=-200, y=200)
    racing = True

while racing:
    for turtle in turtles:
        if turtle.xcor() > 205:
            racing = False
            winner = turtle.pencolor()
            celebrate(turtle)
            if winner == bet:
                t.write(
                    f"Congratulations! The {winner} turtle won!", font=('Arial', 20))
            else:
                t.write(
                    f"Bad luck! The {winner} turtle won!", font=('Arial', 20))
            break
        else:
            distance = randint(2, 12)
            turtle.forward(distance)

screen.exitonclick()
