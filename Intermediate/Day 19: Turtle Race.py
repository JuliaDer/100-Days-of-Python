from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race"
                                             "(red, orange, yellow, green, blue or purple? Enter a color: ")
colors = ["red", "orange", "brown", "green", "blue", "purple"]
y_position = [-80, -50, -20, 10, 40, 70]
all_turtles = []

tim = Turtle()
tim.hideturtle()
style = ('Times', 20, 'bold')


for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                tim.color(winning_color)
                tim.write(f"You've won! The {winning_color} turtle is the winner!", font=style, align="center")
            else:
                tim.color(winning_color)
                tim.write(f"You've lost! The {winning_color} turtle is the winner!", font=style, align='center')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
