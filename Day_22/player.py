from turtle import Turtle, Screen


class Player(Turtle):

    # General attributes

    def __init__(self, screen):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.screen = screen

    def move(self, dire: str):
        new_x = self.pos()[0]
        new_y = self.pos(
        )[1] + 10 if dire == 'up' else self.pos()[1] - 10

        self.goto(new_x, new_y)
        self.screen.update()

    def move_up(self):
        self.move('up')

    def move_down(self):
        self.move('down')


class LeftPlayer(Player):
    def __init__(self, screen):
        # super().__init__(self, 'left')
        super().__init__(screen)
        self.setpos(-350, 0)


class RightPlayer(Player):
    def __init__(self, screen):
        super().__init__(screen)
        self.setpos(350, 0)
