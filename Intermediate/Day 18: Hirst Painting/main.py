# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpeg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
my_turtle = turtle_module.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()

color_list = [(243, 243, 247), (246, 243, 240), (247, 243, 245), (237, 244, 241), (132, 166, 203), (221, 149, 106),
              (198, 135, 147), (33, 42, 60), (42, 104, 153), (166, 57, 47), (237, 212, 92), (141, 183, 163),
              (150, 59, 66), (215, 81, 71), (51, 111, 90), (34, 61, 55), (236, 163, 154), (156, 33, 31),
              (170, 30, 33), (228, 165, 171), (18, 97, 71), (55, 46, 49), (171, 186, 220), (57, 54, 50), (33, 60, 108),
              (184, 103, 114), (108, 126, 157), (176, 199, 189), (33, 151, 210), (64, 65, 59)]

my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.forward(50)

    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
