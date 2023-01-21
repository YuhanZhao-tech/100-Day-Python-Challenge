from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.pensize(10)
run = 100
while run > 0:
    rgb = [random.randint(0, 255) for _ in range(3)]
    tim.pencolor(*rgb)
    tim.setheading(90 * random.randint(1, 4))
    tim.forward(50)
    run -= 1

screen.exitonclick()
