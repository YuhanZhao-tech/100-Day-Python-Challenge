from turtle import Turtle


class SnakePiece():
    def __init__(self, position=[0, 0]):
        self._piece = Turtle(shape='square')
        self._piece.shapesize(1, 1, 0)
        self._piece.penup()
        self._piece.setposition(tuple(position))

        print(self._piece.pos())

    def travel_to(self, position):
        self._piece.goto(tuple(position))
        return self

    def destroy(self):
        self._piece.hideturtle()
