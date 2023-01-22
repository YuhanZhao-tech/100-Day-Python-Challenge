from turtle import Screen
from Snake_piece import SnakePiece
from queue import Queue
import time


class Snake():

    GRID = 22
    _step_queue = Queue()
    _head_position = [0, 0]
    _forward = 'right'
    _gameover = False

    def __init__(self):
        for i in range(3):
            self._step_queue.put(SnakePiece((-self.GRID*(2-i), 0)))

    def set_direction(self, direction):
        self._forward = direction

    def update_head_pos(self):
        pass

    def moving(self, screen):

        while not self._gameover:
            screen.listen()
            vec = {'right': [1, 0], 'left': [-1, 0],
                   'up': [0, 1], 'down': [0, -1]}[self._forward]
            vec = list(map(lambda n: n*self.GRID, vec))
            self._head_position = [
                vec[i]+self._head_position[i] for i in range(2)]

            old_piece = self._step_queue.get()

            self._step_queue.put(old_piece.travel_to(self._head_position))
            time.sleep(0.25)
            screen.update()
