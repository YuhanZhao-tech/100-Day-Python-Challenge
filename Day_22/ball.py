from turtle import Turtle
import time
import random


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.screen = screen

    def move(self):
        self.goto(self.pos()[0] + 10, self.pos()[1] + 10)
