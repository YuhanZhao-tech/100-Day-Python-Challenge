from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

screen.setup(width=900, height=900, startx=0, starty=0)
for i in range(4):
    for _ in range(5):

        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

    turtle.left(90)

screen.exitonclick()
