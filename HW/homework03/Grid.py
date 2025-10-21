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

    @staticmethod
    def check_list_malformed(lst):
        if lst is None:
            raise ValueError("List is None")
        elif not isinstance(lst, list):
            raise ValueError("Input is not a list")
        elif len(lst) == 0:
            raise ValueError("List is empty")
        elif not all(isinstance(row, list) for row in lst):
            raise ValueError("List contains non-lists")
        elif not all(len(row) == len(lst[0]) for row in lst):
            raise ValueError("List rows are not all the same length")
        return True

    @staticmethod
    def build(lst):
        if not Grid.check_list_malformed(lst):
            raise ValueError("List is malformed")
        grid = Grid(len(lst[0]), len(lst))
        for y in range(len(lst)):
            for x in range(len(lst[0])):
                grid.set(x, y, lst[y][x])
        return grid

    def copy(self):
        new_grid = Grid.build(self.array)
        return new_grid

    def __str__(self):
        return f"Grid({self.width}, {self.height}, first = {self.get(0, 0)})"

    def __repr__(self):
        return f"Grid.build({self.array})"

    def __eq__(self, other):
        if not (isinstance(other, Grid) or isinstance(other, list)):
            return False
        elif isinstance(other, list):
            return self.array == other
        return self.array == other.array

