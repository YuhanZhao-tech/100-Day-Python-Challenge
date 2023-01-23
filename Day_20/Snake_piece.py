from turtle import Turtle


class SnakePiece():
    def __init__(self, position=[0, 0]):
        self._piece = Turtle(shape='square')
        self._piece.shapesize(1, 1, 5)
        self._piece.penup()
        self._piece.setposition(tuple(position))

    def travel_to(self, position):
        self._piece.goto(tuple(position))
        return self

    def destroy(self):
        self._piece.hideturtle()

    def get_coordinate(self):
        return self._piece.position()


class StageTurtle(SnakePiece):
    def __init__(self):
        super().__init__(position=[-418, -418])
        self._piece.pendown()
        self._piece.pensize(width=44)
        for i in range(4):
            self._piece.forward(836)
            self._piece.left(90)
