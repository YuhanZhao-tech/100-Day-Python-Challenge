from Snake import Snake
from turtle import Screen

screen = Screen()
screen.tracer(n=0)
snake = Snake()


def right():
    snake.set_direction('right')


def left():
    snake.set_direction('left')


def up():
    snake.set_direction('up')


def down():
    snake.set_direction('down')


screen.onkeypress(fun=right, key='d')
screen.onkeypress(fun=left, key='a')
screen.onkeypress(fun=up, key='w')
screen.onkeypress(fun=down, key='s')
snake.moving(screen)
