from colorgram import *
import random
import os
from turtle import Turtle, Screen

# dirname = os.path.dirname(__file__)
# print(f"current path {dirname}\n{__file__}")
# sample_pic = open(os.path.join(dirname, "Sample_art.jpg"))
colors = colorgram.extract(f"{os.path.dirname(__file__)}\Sample_art.jpg", 20)

tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.setworldcoordinates(-1, -1, screen.window_width() -
                           1, screen.window_height() - 1)
screen_size = screen.screensize()[0]


def draw_dot_art(row):
    step = screen_size/(row-1)
    start_pos = (step for i in range(2))
    tim.penup()
    for i in range(row):
        for j in range(row):
            dot_col = random.choice(colors).rgb
            tim.pendown()
            tim.dot(300/row, dot_col)
            tim.penup()
            if not j == row-1:
                tim.forward(step)

        tim.setheading(90)
        tim.forward(step)
        tim.setheading(((i+1) % 2)*180)


draw_dot_art(10)
screen.exitonclick()
