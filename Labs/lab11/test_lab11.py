from byu_pytest_utils import max_score, with_import
import pytest


def build_grid(Grid, lst):
    assert isinstance(lst, list)
    height = len(lst)
    assert height != 0
    for row in lst:
        assert isinstance(row, list)
    width = len(lst[0])
    for row in lst[1:]:
        assert len(row) == width

    grid = Grid(width, height)
    for y, row in zip(range(height), lst):
        for x, space in zip(range(width), row):
            grid.set(x, y, space)
    return grid

@max_score(2)
@with_import('Grid', 'Grid')
def test_in_bounds(Grid):
    grid = Grid(2, 5)

    assert grid.in_bounds(1, 4)
    assert grid.in_bounds(0, 2)
    assert grid.in_bounds(0, 0)

    assert not grid.in_bounds(-1, 0)
    assert not grid.in_bounds(2, 3)
    assert not grid.in_bounds(0, -1)
    assert not grid.in_bounds(1, 5)


@max_score(3)
@with_import('Grid', 'Grid')
def test_get_and_set(Grid):
    grid = Grid(3, 4)

    key = [[(x, y) for x in range(grid.width)] for y in range(grid.height)]

    for y in range(grid.height):
        for x in range(grid.width):
            grid.set(x, y, (x, y))

    for y in range(grid.height):
        for x in range(grid.width):
            assert grid.get(x, y) == key[y][x]

    assert grid.array == key

@max_score(3)
@with_import('Grid', 'Grid')
def test_get_set_out_of_bounds(Grid):
    grid = Grid(3, 3)
    for y in range(3):
        for x in range(3):
            grid.get(x, y)
            grid.set(x, y, None)

    for y in range(-1, 4):
        with pytest.raises(IndexError):
            grid.get(-1, y)
            pytest.fail(f"{grid}.get(-1, {y}) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(-1, y, None)
            pytest.fail(f"{grid}.set(-1, {y}, None) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.get(3, y)
            pytest.fail(f"{grid}.get(3, {y}) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(3, y, None)
            pytest.fail(f"{grid}.set(3, {y}, None) didn't raise an exception")

    for x in range(-1, 4):
        with pytest.raises(IndexError):
            grid.get(x, -1)
            pytest.fail(f"{grid}.get({x}, -1) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(x, -1, None)
            pytest.fail(f"{grid}.set({x}, -1, None) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.get(x, 3)
            pytest.fail(f"{grid}.get({x}, 3) didn't raise an exception")
        with pytest.raises(IndexError):
            grid.set(x, 3, None)
            pytest.fail(f"{grid}.set({x}, 3, None) didn't raise an exception")


@max_score(5)
@with_import('Grid', 'Grid')
def test_str_and_repr(Grid):
    grid = Grid(6, 2)

    assert str(grid) == "Grid(6, 2, first = None)"
    assert repr(grid) == "Grid(6, 2, first = None)"

    grid.set(0, 0, 1)

    assert str(grid) == "Grid(6, 2, first = 1)"
    assert repr(grid) == "Grid(6, 2, first = 1)"


@max_score(7)
@with_import('Grid', 'Grid')
def test_eq(Grid):
    grid1 = build_grid(Grid, [[1, 1, 1], [2, 3, 5], [1, 1, 1], [1, 4, 2]])
    grid2 = build_grid(Grid, [[1, 1, 1, 2], [3, 5, 1, 1], [1, 1, 4, 2]])
    grid3 = build_grid(Grid, [[5, 2, 3], [3, 4, 1], [1, 2, 4], [3, 4, 2]])
    grid4 = build_grid(Grid, [[1, 1, 1], [2, 3, 5], [1, 1, 1], [1, 4, 2]])
    grid5 = build_grid(Grid, [[1, 1, 1], [2, 3, 5]])
    grid6 = build_grid(Grid, [[5, 5, 2], [4, 1, 5]])

    assert grid1 != None
    assert grid1 != 1
    assert grid1 != 'string'

    assert grid1 != grid2
    assert grid1 != grid3
    assert grid1 == grid4
    assert grid1 != grid5
    assert grid1 != grid6

    assert grid2 != grid3
    assert grid2 != grid4
    assert grid2 != grid5
    assert grid2 != grid6

    assert grid3 != grid4
    assert grid3 != grid5
    assert grid3 != grid6

    assert grid4 != grid5
    assert grid4 != grid6

    assert grid5 != grid6
