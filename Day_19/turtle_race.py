from turtle import Turtle, Screen
import random

color_string = ['red', 'green', 'cyan', 'yellow', 'magenta']
turtles = [Turtle() for _ in range(5)]

for turtle in turtles:
    turtle.shape('turtle')
    turtle.resizemode('user')
    turtle.shapesize(2, 2, 1.5)
screen = Screen()

for i in range(len(turtles)):
    turtles[i].penup()
    turtles[i].fillcolor(color_string[i])

    turtles[i].setposition(-(screen.window_width()/2 - 100), 100 - 50*i)


def move_turtle(turtle, step):
    turtle.forward(step)


def race():
    user_guess = screen.textinput(
        "Who's going to win?", "guess the color of the winner, {}".format(color_string))

    race_finish = False
    winner = None

    while not race_finish:
        turtle = random.choice(turtles)
        move_turtle(turtle, 10)
        if turtle.pos()[0] > screen.window_width()/2 - 100:
            race_finish = True
            winner = turtle

    winner_color = winner.fillcolor()
    print("You {}! The winner is {}".format(
        'win' if user_guess == winner_color else 'loose', winner_color))


race()

screen.listen()
screen.exitonclick()
