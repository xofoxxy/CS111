from byu_pytest_utils import max_score, with_import
from pytest import xfail


@max_score(4)
@with_import('lab16', 'berry_finder')
@with_import('lab16', 'Tree')
def test_berry_finder(Tree, berry_finder):
    scrat = Tree('berry')
    assert berry_finder(scrat)

    sproul = Tree(
        'roots', [Tree('branch1', [Tree('leaf'), Tree('berry')]), Tree('branch2')])
    assert berry_finder(sproul)

    numbers = Tree(
        1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    assert not berry_finder(numbers)

    t = Tree(1, [Tree('berry', [Tree('not berry')])])
    assert berry_finder(t)


@max_score(4)
@with_import('lab16', 'height')
@with_import('lab16', 'Tree')
def test_height(Tree, height):
    t = Tree(3)
    assert height(t) == 0

    t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    assert height(t) == 2

    t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
    assert height(t) == 3


@max_score(6)
@with_import('lab16', 'max_path_sum')
@with_import('lab16', 'Tree')
def test_max_path_sum(Tree, max_path_sum):
    t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    assert max_path_sum(t) == 11

    t = Tree(12, [Tree(9, [Tree(7), Tree(6, [Tree(8)]), Tree(15)]),
             Tree(10, [Tree(6)]), Tree(7), Tree(12, [Tree(6), Tree(7), Tree(8)])])
    assert max_path_sum(t) == 36


@max_score(6)
@with_import('lab16', 'find_path')
@with_import('lab16', 'Tree')
def test_find_path(Tree, find_path):
    t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(15)])
    assert find_path(t, 2) == [2]
    assert find_path(t, 3) == [2, 7, 3]
    assert find_path(t, 5) == [2, 7, 6, 5]
    assert find_path(t, 10) is None


@max_score(0)
def test_has_path():
    try:
        @with_import('lab16', 'has_path')
        @with_import('lab16', 'Tree')
        def inner_has_path(Tree, has_path):
            greetings = Tree('h', [Tree('i'),
                            Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
                            Tree('y')])])

            assert has_path(greetings, 'h') is True
            assert has_path(greetings, 'i') is False
            assert has_path(greetings, 'hi') is True
            assert has_path(greetings, 'hello') is True
            assert has_path(greetings, 'hey') is True
            assert has_path(greetings, 'bye') is False
            assert has_path(greetings, 'hint') is False
        inner_has_path()

    except Exception as e:
        xfail(f"\nOPTIONAL: has_path() is not implemented correctly:\n{e}")
