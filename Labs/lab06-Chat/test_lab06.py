"""
test_lab06.py

Pytest tests written BEFORE code (TDD) for:
- product, summation
- square, sqrt, mean, median, mode, stdev
- stat_analysis

Run one test at a time if desired:
    pytest test_lab06.py::test_summation
    pytest test_lab06.py::test_product
"""

import pytest
from math import isclose
from pytest import approx

import lab06


# ------------------------
# Q1: Product & Summation
# ------------------------

def test_product_invalid_inputs():
    with pytest.raises(ValueError):
        lab06.product(0)
    with pytest.raises(ValueError):
        lab06.product(-5)
    with pytest.raises(ValueError):
        lab06.product(3.2)  # not an int
    with pytest.raises(ValueError):
        lab06.product("4")  # not an int


def test_product_valid_small():
    assert lab06.product(1) == 1
    assert lab06.product(2) == 2
    assert lab06.product(3) == 6
    assert lab06.product(5) == 120


def test_summation_invalid_inputs():
    with pytest.raises(ValueError):
        lab06.summation(-1)
    with pytest.raises(ValueError):
        lab06.summation(2.5)
    with pytest.raises(ValueError):
        lab06.summation("10")


def test_summation_valid():
    assert lab06.summation(0) == 0
    assert lab06.summation(1) == 1
    assert lab06.summation(5) == 15
    assert lab06.summation(10) == 55


# ------------------------
# Q2: Statistics helpers
# ------------------------

def test_square_basic():
    assert lab06.square(0) == 0
    assert lab06.square(2) == 4
    assert lab06.square(-3) == 9
    assert lab06.square(1.5) == approx(2.25)


def test_sqrt_basic():
    assert lab06.sqrt(0) == 0
    assert lab06.sqrt(1) == 1
    assert lab06.sqrt(4) == 2
    assert lab06.sqrt(2) == approx(1.41421356237, rel=1e-12, abs=1e-12)
    with pytest.raises(ValueError):
        lab06.sqrt(-1)


def test_mean_validation():
    with pytest.raises(ValueError):
        lab06.mean([])
    with pytest.raises(TypeError):
        lab06.mean([1, "a", 3])


def test_mean_values():
    assert lab06.mean([1]) == 1
    assert lab06.mean([1, 2, 3, 4]) == 2.5
    assert lab06.mean([1, 1, 1, 3, 4]) == 2.0
    assert lab06.mean([0.5, 1.5]) == 1.0


def test_median_validation():
    with pytest.raises(ValueError):
        lab06.median([])
    with pytest.raises(TypeError):
        lab06.median([1, 2, "x"])


def test_median_values():
    assert lab06.median([3]) == 3.0
    assert lab06.median([1, 2, 3]) == 2.0
    assert lab06.median([1, 2, 3, 4]) == 2.5
    assert lab06.median([5, 1, 4, 2, 3]) == 3.0  # unsorted input


def test_mode_validation():
    with pytest.raises(ValueError):
        lab06.mode([])
    with pytest.raises(TypeError):
        lab06.mode([1, 2, "z"])


def test_mode_values_and_tie_break():
    assert lab06.mode([1]) == 1
    assert lab06.mode([1, 2, 2, 3]) == 2
    # Tie -> first to reach highest count wins
    assert lab06.mode([1, 1, 2, 2]) == 1
    assert lab06.mode([2, 2, 1, 1]) == 2
    assert lab06.mode([3, 1, 3, 1, 2, 1]) == 1


def test_stdev_validation():
    with pytest.raises(ValueError):
        lab06.stdev([])
    with pytest.raises(TypeError):
        lab06.stdev([1, 2, "q"])


def test_stdev_population():
    # population stdev for [1,2,3,4] -> sqrt(1.25) ~ 1.11803398875
    assert lab06.stdev([1, 2, 3, 4]) == approx(1.11803398875, rel=1e-12, abs=1e-12)
    # single element -> 0
    assert lab06.stdev([5]) == 0.0
    # mixed floats
    assert lab06.stdev([0.5, 1.5]) == approx(0.5, rel=1e-12, abs=1e-12)


def test_stat_analysis_happy_path():
    data = [1, 2, 2, 3, 4]
    out = lab06.stat_analysis(data)
    assert isinstance(out, dict)
    assert set(out.keys()) == {"mean", "median", "mode", "stdev"}
    assert out["mean"] == approx(2.4, rel=1e-12, abs=1e-12)
    assert out["median"] == 2.0
    assert out["mode"] == 2
    # compute expected population stdev manually:
    # mean=2.4; deviations squared: (1-2.4)^2=1.96, (2-2.4)^2=0.16, (2-2.4)^2=0.16,
    # (3-2.4)^2=0.36, (4-2.4)^2=2.56; sum=5.2; /5=1.04; sqrt=~1.019803903
    assert out["stdev"] == approx(1.019803903, rel=1e-12, abs=1e-12)


def test_stat_analysis_invalid_inputs():
    with pytest.raises(ValueError):
        lab06.stat_analysis([])
    with pytest.raises(TypeError):
        lab06.stat_analysis([1, 2, "x"])
