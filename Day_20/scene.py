from Snake import Snake
from Snake_piece import SnakePiece, StageTurtle
from turtle import Screen

screen = Screen()
screen.screensize(bg='yellow')
screen.setup(836, 836)
screen.setworldcoordinates(-418, -418, 418, 418)
# screen_size_to_grid =
screen.tracer(n=0)
stage_turtle = StageTurtle()
screen.update()
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
