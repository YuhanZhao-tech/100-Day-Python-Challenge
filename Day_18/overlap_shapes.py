from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)

tim = Turtle()
start_pos = tim.position()
for shape in range(1, 9):

    rgb = []
    for i in range(3):
        rgb.append(randint(0, 255))

    tim.pencolor(*rgb)
    for sides in range(shape+2):
        tim.forward(100)
        tim.right(360/(shape+2))


screen.exitonclick()
