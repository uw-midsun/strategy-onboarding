import pytest
from ..q2_debugging import adjacent_subtraction, str_math


def test_adjacent_subtraction():
    assert adjacent_subtraction([1, 6, 3, 2, 8]) == [5, -3, -1, 6]
    assert adjacent_subtraction([1, 2, 3, 4]) == [1, 1, 1, 1]
    assert adjacent_subtraction([1]) == [1]
    assert adjacent_subtraction([]) == None


def test_str_math():
    assert str_math(["1", "6", "3", "2", "8"]) == 20
    assert str_math(["1", "b", "3", "-2", []]) == 2
    assert str_math(["1", "b", "3.5", "-12"]) == -7.5
    assert str_math(["hi"]) == None
    assert str_math([]) == None
