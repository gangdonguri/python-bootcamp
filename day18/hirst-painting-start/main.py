# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

import turtle as t
import random

def turtle_row_move(i):
    for y in range(1, 11):
        timmy_the_turtle.pendown()
        timmy_the_turtle.color(random.choice(color_list))
        timmy_the_turtle.stamp()
        timmy_the_turtle.penup()
        if y == 10:
            turtle_column_move(i)
        else:
            timmy_the_turtle.forward(50)

def turtle_column_move(i):
    timmy_the_turtle.penup()
    add_y = 50 * i
    if i != 10:
        timmy_the_turtle.setpos(-250, -250 + add_y)
    else:
        timmy_the_turtle.hideturtle()

t.colormode(255)
timmy_the_turtle = t.Turtle()
timmy_the_turtle.speed(10)
timmy_the_turtle.shape("circle")
timmy_the_turtle.turtlesize(1, 1)

timmy_the_turtle.penup()
timmy_the_turtle.setpos(-250, -250)

for i in range(1, 11):
    turtle_row_move(i)

screen = t.Screen()
screen.exitonclick()