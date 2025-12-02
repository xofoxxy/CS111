from byu_pytest_utils import max_score, with_import, test_files


@max_score(5)
@with_import('lab17', 'load_grid')
def test_load_grid(load_grid):
    grid_1 = [
        ['C', 'A', 'T'],
        ['R', 'R', 'E'],
        ['D', 'O', 'G']
    ]
    grid_2 = [
        ['A', 'J', 'E', 'L', 'X'],
        ['K', 'C', 'A', 'R', 'D'],
        ['Z', 'I', 'T', 'E', 'O'],
        ['M', 'U', 'S', 'E', 'P'],
        ['T', 'Y', 'N', 'Q', 'W']
    ]


    assert load_grid(test_files / 'grid1.txt') == grid_1
    assert load_grid(test_files / 'grid2.txt') == grid_2


@max_score(7.5)
@with_import('lab17', 'load_grid')
@with_import('lab17', 'exists')
def test_exists_1(exists, load_grid):
    grid = load_grid(test_files / 'grid1.txt')

    assert exists(grid, 'DOG')
    assert exists(grid, 'CAT')
    assert exists(grid, 'CAR')
    assert exists(grid, 'CARE')
    assert not exists(grid, 'CART')


@max_score(7.5)
@with_import('lab17', 'load_grid')
@with_import('lab17', 'exists')
def test_exists_2(exists, load_grid):
    grid = load_grid(test_files / 'grid2.txt')

    assert exists(grid, 'CARD')
    assert exists(grid, 'MUSE')
    assert exists(grid, 'POET')
    assert exists(grid, 'STEEP')
    assert not exists(grid, 'SITE')
    assert not exists(grid, 'SIDE')

