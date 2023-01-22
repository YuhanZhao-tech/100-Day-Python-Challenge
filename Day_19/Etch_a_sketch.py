# Etch-A-Sketch
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fw():
    tim.forward(5)


def move_bw():
    tim.backward(5)


def turn_lt():
    tim.setheading(tim.heading() + 10)


def turn_rt():
    tim.setheading(tim.heading() - 10)


def clear_reset():
    tim.clear()
    tim.penup()
    tim.setposition(0, 0)
    tim.setheading(0)
    tim.pendown()


screen.onkeypress(fun=move_fw, key="w")
screen.onkeypress(fun=move_bw, key='s')
screen.onkeypress(fun=turn_lt, key='a')
screen.onkeypress(fun=turn_rt, key='d')
screen.onkeypress(fun=clear_reset, key='c')


screen.listen()
screen.exitonclick()
