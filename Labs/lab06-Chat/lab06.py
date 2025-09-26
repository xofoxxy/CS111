"""
lab06.py

Implementations for Lab 06: products/summations and basic statistics.
Followed by small, explicit input validation per the spec.
"""

from typing import Iterable, List, Sequence, Dict, Any
import math


# ------------------------
# Q1: Product & Summation
# ------------------------

def product(n: int) -> int:
    """
    Return 1*2*...*n for integer n >= 1.
    Raise ValueError if n < 1 or not an integer.
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer >= 1")
    if n < 1:
        raise ValueError("n must be >= 1")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def summation(n: int) -> int:
    """
    Return 1 + 2 + ... + n for integer n >= 0.
    Raise ValueError if n < 0 or not an integer.
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer >= 0")
    if n < 0:
        raise ValueError("n must be >= 0")
    # arithmetic series formula also works, but keep it explicit for clarity
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# ------------------------
# Q2: Statistics helpers
# ------------------------

def _ensure_numeric_iterable(xs: Iterable[Any]) -> list:
    try:
        lst = list(xs)
    except TypeError:
        raise TypeError("Input must be an iterable of numbers.")
    if len(lst) == 0:
        raise ValueError("Input must be a non-empty iterable.")
    for x in lst:
        if not isinstance(x, (int, float)):
            raise TypeError("All elements must be int or float.")
    return lst


def square(x: float) -> float:
    return x * x


def sqrt(x: float) -> float:
    if x < 0:
        raise ValueError("sqrt undefined for negative numbers")
    return math.sqrt(x)


def mean(xs: Iterable[float]) -> float:
    lst = _ensure_numeric_iterable(xs)
    return sum(lst) / len(lst)


def median(xs: Iterable[float]) -> float:
    lst = _ensure_numeric_iterable(xs)
    s = sorted(lst)
    n = len(s)
    mid = n // 2
    if n % 2 == 1:
        return float(s[mid])
    else:
        return (s[mid - 1] + s[mid]) / 2.0


def mode(xs: Iterable[float]):
    """
    Return the most common element. If there is a tie,
    return the element that first reached the highest count in the original order.
    Example: [1,1,2,2] -> 1
    """
    lst = _ensure_numeric_iterable(xs)
    counts: Dict[Any, int] = {}
    best = None
    best_count = 0
    for x in lst:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] > best_count:
            best = x
            best_count = counts[x]
    return best


def stdev(xs: Iterable[float]) -> float:
    """
    Population standard deviation (divide by n, not n-1).
    """
    lst = _ensure_numeric_iterable(xs)
    mu = mean(lst)
    total = 0.0
    for x in lst:
        dx = x - mu
        total += dx * dx
    return sqrt(total / len(lst))


def stat_analysis(xs: Iterable[float]) -> Dict[str, float]:
    """
    Return a dictionary with mean, median, mode, and stdev for the dataset.
    Propagates the same input validation as the underlying functions.
    """
    lst = _ensure_numeric_iterable(xs)
    return {
        "mean": mean(lst),
        "median": median(lst),
        "mode": mode(lst),
        "stdev": stdev(lst),
    }
