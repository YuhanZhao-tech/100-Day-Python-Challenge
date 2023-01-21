import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
tim.speed('fastest')


def spirograph(num_circle):

    for _ in range(num_circle):
        color = (random.randint(0, 255) for _ in range(3))
        t.pencolor(color)
        t.circle(100)
        t.left(360/num_circle)


spirograph(50)
screen.exitonclick()
