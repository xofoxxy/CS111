class Particle:
    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.x = x
        self.y = y
        self.grid.set(self.x, self.y, self)

    def move(self):
        physics_value = self.physics()
        if physics_value is None:
            return
        elif type(physics_value) is tuple:
            self.grid.set(self.x, self.y, None)
            x, y = physics_value
            self.x = x
            self.y = y
            self.grid.set(self.x, self.y, self)
            return

    def __eq__(self, other):
        if not isinstance(other, Particle):
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"{type(self).__name__}({self.x},{self.y})"
