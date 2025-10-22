from Particle import Particle
from Grid import Grid


class Sand(Particle):
    def is_move_ok(self, x, y):
        ok_spaces = [None]
        diagonal_move = False if (self.x == x) else True
        try:
            if self.grid.get(x, y) in ok_spaces and not diagonal_move:
                return True
        except IndexError:
            print("Index Error 1")
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
        for possible_move in movement_priorities:
            if self.is_move_ok(*possible_move):
                return possible_move
        return None


if __name__ == "__main__":
    grid = Grid(1,2)
    sand = Sand(grid, 0,0)
    grid.print()
    input()

    sand.move()
    grid.print()