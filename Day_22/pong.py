from turtle import Screen
from player import LeftPlayer, RightPlayer
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

left = LeftPlayer(screen)
right = RightPlayer(screen)
ball = Ball(screen)

screen.onkeypress(left.move_up, 'w')
screen.onkeypress(left.move_down, 's')
screen.onkeypress(right.move_up, 'Up')
screen.onkeypress(right.move_down, 'Down')
screen.listen()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
screen.exitonclick()
