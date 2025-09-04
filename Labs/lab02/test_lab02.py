from byu_pytest_utils import max_score, this_folder, with_import, ensure_missing
from pytest import xfail
from pathlib import Path


@max_score(3)
@with_import('lab02', 'even_weighted')
def test_even_weighted_1(even_weighted):
    assert even_weighted([1, 2, 3, 4, 5, 6]) == [0, 6, 20]


@max_score(3)
@with_import('lab02', 'even_weighted')
def test_even_weighted_2(even_weighted):
    assert even_weighted([9, 17, 4, 5, 4]) == [0, 8, 16]


@max_score(3)
@with_import('lab02', 'couple')
def test_couple_1(couple):
    assert couple([1, 2, 3], [4, 5, 6]) == [[1, 4], [2, 5], [3, 6]]


@max_score(3)
@with_import('lab02', 'couple')
def test_couple_2(couple):
    assert couple(['c', 6], ['s', '1']) == [['c', 's'], [6, '1']]


@max_score(8)
@with_import('lab02', 'copy_file')
@ensure_missing(this_folder / 'output.txt')
def test_copy_file(copy_file):
    KEY = """1: They say you should never eat dirt.
2: It's not nearly as good as an onion.
3: It's not as good as the CS pun on my shirt."""
    copy_file(this_folder / 'text.txt', this_folder / 'output.txt')
    with open(this_folder / 'output.txt', 'r') as fin:
        assert fin.read() == KEY
    Path.unlink(this_folder / 'output.txt', missing_ok=True)

@max_score(0)
def test_factors_list():
    try:
        @with_import('lab02', 'factors_list')
        def inner_factors_list(factors_list):
            assert factors_list(3) == [1]
            assert factors_list(4) == [1, 2]
            assert factors_list(9) == [1, 3]
            assert factors_list(10) == [1, 2, 5]
            assert factors_list(12) == [1, 2, 3, 4, 6]
            assert factors_list(16) == [1, 2, 4, 8]
            assert factors_list(17) == [1]
            assert factors_list(18) == [1, 2, 3, 6, 9]
            assert factors_list(20) == [1, 2, 4, 5, 10]
        inner_factors_list()
    except Exception as e:
        xfail(f'\nOPTIONAL: factors_list() is not implemented correctly:\n{e}')
