from turtle import Screen
from Snake_piece import SnakePiece
from queue import Queue
import time
import random


class Snake():

    GRID = 22
    _step_queue = Queue()
    _head_position = [0, 0]
    _forward = 'right'
    _gameover = False
    _objective = False
    _obj_piece = None
    _score = 0
    _stage = 1
    _wait = 0.25

    def __init__(self):
        for i in range(3):
            self._step_queue.put(SnakePiece((-self.GRID*(2-i), 0)))

    def set_direction(self, direction):
        self._forward = direction

    def check_gameover(self):
        x = self._head_position[0]
        y = self._head_position[1]
        if x > 418 or x < -418 or y > 418 or y < -418:
            self._gameover = True

        for body in self._step_queue.queue:
            if list(body.get_coordinate()) == self._head_position:
                self._gameover = True
                return

    def moving(self, screen):

        while not self._gameover:

            # Spawn objective if not exist
            if not self._objective:
                self._obj_piece = self.spawn_piece()
                self._objective = True
            # listen the key input
            screen.listen()

            # Set speed base on score
            self.set_speed(screen)

            # update head position
            vec = {'right': [1, 0], 'left': [-1, 0],
                   'up': [0, 1], 'down': [0, -1]}[self._forward]
            vec = list(map(lambda n: n*self.GRID, vec))
            self._head_position = [
                vec[i]+self._head_position[i] for i in range(2)]

            if self.check_obj_achieved():
                self._step_queue.put(self._obj_piece)
                self._objective = False
                self._score += 1
                screen.title("Score = {}, Stage = {}".format(
                    self._score, self._stage))
                time.sleep(0.25)
                continue

            # if head reached wall, stop
            self.check_gameover()
            if self._gameover:
                print('gameover')
                break

            # every frame take one piece on the back and put it in the head position
            old_piece = self._step_queue.get()
            self._step_queue.put(old_piece.travel_to(self._head_position))
            time.sleep(self._wait)
            screen.update()

        screen.textinput('Game over',
                         'Game over! Your final score is {}'.format(self._score))

    def spawn_piece(self):
        new_piece = SnakePiece([random.randint(-17, 17)*22 for _ in range(2)])
        return new_piece

    def check_obj_achieved(self):
        return self._head_position == list(self._obj_piece.get_coordinate())

    def set_speed(self, screen):
        if self._score < 10:
            self._wait = 0.25
            self._stage = 1
        elif self._score < 20:
            self._wait = 0.15
            self._stage = 2
            screen.screensize(bg='#BFD7EA')
        else:
            self._wait = 0.1
            self._stage = 3
            screen.screensize(bg='#FF6663')
