import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a clolr: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
winning_color = ""
alt_turtles = []
co_winner = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y_coordinate = -125 + 50 * turtle_index
    new_turtle.goto(x=-230, y=y_coordinate)
    alt_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in alt_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            co_winner.append(winning_color)

        rand_distance = random.randint(0. 10)
        turtle.forward(rand_distance)

if len(co_winner) >= 2:
    if user_bet in co_winner:
        print(f"You've won! The {co_winner} turtle is the co-winner!")
    else:
        print(f"You've lost! The {co_winner} turtle is the co-winner!")
else:
    if user_bet == winning_color:
        print(f"You've won! The {winning_color} turtle is the winner!")
    else:
        print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()