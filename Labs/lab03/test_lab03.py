from byu_pytest_utils import max_score, with_import
from pytest import approx

@max_score(2)
@with_import('lab03', 'average_temperature')
def test_average_temperature_1(average_temperature):
    assert average_temperature([72.2, 68.7, 67.4, 77.3, 81.6, 83.7]) == approx(75.15)

@max_score(3)
@with_import('lab03', 'average_temperature')
def test_average_temperature_2(average_temperature):
    assert average_temperature([63.4, 70.8, 52.3, 74.6, 69.2, 54.3]) == approx(64.1)

@max_score(2)
@with_import('lab03', 'hot_days')
def test_hot_days_1(hot_days, capfd):
    result = hot_days([72.2, 68.7, 67.4, 77.3, 81.6, 83.7])
    out, err = capfd.readouterr()

    assert out == "There were 2 day(s) more than 5 degrees above the average of 75.2.\n"
    assert result == 2

@max_score(2)
@with_import('lab03', 'hot_days')
def test_hot_days_2(hot_days, capfd):
    result = hot_days([63.4, 70.8, 52.3, 74.6, 69.2, 54.3])
    out, err = capfd.readouterr()

    assert out == "There were 3 day(s) more than 5 degrees above the average of 64.1.\n"
    assert result == 3

@max_score(2.5)
@with_import('lab03', 'is_palindrome')
def test_is_palindrome_true(is_palindrome, capfd):
    result = is_palindrome('rotator')
    out, err = capfd.readouterr()

    assert out == 'rotator is a palindrome.\n'
    assert result

@max_score(2.5)
@with_import('lab03', 'is_palindrome')
def test_is_palindrome_false(is_palindrome, capfd):
    result = is_palindrome('apple')
    out, err = capfd.readouterr()

    assert out == 'apple is not a palindrome.\n'
    assert not result

@max_score(3)
@with_import('lab03', 'even_weighted')
def test_even_weighted_1(even_weighted):
    assert even_weighted([1, 2, 3, 4, 5, 6]) == [0, 6, 20]

@max_score(3)
@with_import('lab03', 'even_weighted')
def test_even_weighted_2(even_weighted):
    assert even_weighted([9, 17, 4, 5, 4]) == [0, 8, 16]
