class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = [[None for _ in range(width)] for _ in range(height)]
        print(self.array)

    def in_bounds(self, x, y):
        distance_x = self.width - x
        distance_y = self.height - y
        return 0 < distance_x <= self.width and 0 < distance_y <= self.height

    def get(self, x, y):
        if not self.in_bounds(x, y):
            raise IndexError(f"({x}, {y}) is out of bounds")
        return self.array[y][x]

    def set(self, x, y, value):
        if not self.in_bounds(x, y):
            raise IndexError(f"({x}, {y}) is out of bounds")
        self.array[y][x] = value

    def __str__(self):
        return f"Grid({self.width}, {self.height}, first = {self.get(0, 0)})"

    def __repr__(self):
        return f"Grid({self.width}, {self.height}, first = {self.get(0, 0)})"

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.array == other.array
