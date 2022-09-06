# import colorgram
import turtle as t
from random import choice

# colours = colorgram.extract("hirst-spot-painting.jpg", 22)

# colour_list = []

# for i in colours:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_tuple = (r, g, b)
#     colour_list.append((new_tuple))

colour_list = [(236, 35, 108), (145, 28, 64), (239, 75, 35), (6, 148, 93), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253,
                                                                                                                                                            223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (223, 216, 171), (207, 226, 233), (241, 235, 178)]

print("Create your own Damien Hirst Style Dot Painting!\n(and become a millionaire?)")
columns = int(input("How many dots would you like in each row? "))
rows = int(input("And how many lines of dots would you like? "))
print("Click on the picture to close it.")

a = t.Turtle()
t.colormode(255)


a.pensize(25)


def create_dot_painting(dots, lines):
    y = lines * -20
    x = dots * -22.5
    while y < lines * 30:
        a.penup()
        a.setposition(x, y)
        for _ in range(dots):
            a.color(choice(colour_list))
            a.pendown()
            a.forward(1)
            a.penup()
            a.forward(50)

        y += 50

    a.hideturtle()


create_dot_painting(columns, rows)

s = t.Screen()
s.exitonclick()
