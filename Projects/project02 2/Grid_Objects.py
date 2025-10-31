from Particle import Particle
from Grid import Grid
import random

class Sand(Particle):
    def is_move_ok(self, x, y):
        ok_spaces = [None]
        diagonal_move = False if (self.x == x) else True
        try:
            if self.grid.get(x, y) in ok_spaces and not diagonal_move:
                return True
        except IndexError:
            return False
        try:
            if self.grid.get(x, y) in ok_spaces and self.grid.get(x, y-1) in ok_spaces:
                return True
            return False
        except IndexError:
            print("Index Error 2")
            return True

    def physics(self):
        movement_priorities = [
            (self.x, self.y + 1),
            (self.x - 1, self.y + 1),
            (self.x + 1, self.y + 1)
        ]
        movement_priorities_copy = movement_priorities.copy()
        for possible_move in movement_priorities_copy:
            if self.is_move_ok(*possible_move):
                return possible_move
            else:
                movement_priorities_copy.remove(possible_move)
                random.shuffle(movement_priorities_copy)
        return None


class Rock(Particle):

    @staticmethod
    def physics():
        return None


class Bubble(Particle):
    def is_move_ok(self, x, y):
        ok_spaces = [None]
        diagonal_move = False if (self.x == x) else True
        try:
            if self.grid.get(x, y) in ok_spaces and not diagonal_move:
                return True
        except IndexError:
            return False
        try:
            if self.grid.get(x, y) in ok_spaces and self.grid.get(x, y+1) in ok_spaces:
                return True
        except IndexError:
            return True
        return False

    def physics(self):
        if isinstance(self.grid.get(self.x, self.y + 1), Sand):
            self.grid.set(self.x, self.y + 1, None)
            new_rock = Rock(self.grid, self.x, self.y + 1)
            self.grid.set(self.x, self.y + 1, new_rock)
            self.grid.set(self.x, self.y, None)
            return None

        movement_priorities = [
            (self.x, self.y - 1),
            (self.x + 1, self.y - 1),
            (self.x - 1, self.y - 1),
        ]
        movement_priorities_copy = movement_priorities.copy()
        for possible_moves in movement_priorities_copy:
            if self.is_move_ok(*possible_moves):
                return possible_moves
            else:
                movement_priorities_copy.remove(possible_moves)
                random.shuffle(movement_priorities_copy)
        return None


