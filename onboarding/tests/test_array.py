import pytest
from ..array import find_min_index, reverse_str_arr


def test_array_find_min_index():
    assert(find_min_index([1, 33, 1, -2, 0]) == 3)
    assert(find_min_index([0, 0, 0, 0, 0]) == 0)
    assert(find_min_index([1, 2, 3, 4, 5, 0]) == 5)


def test_reverse_str_arr():
    assert (reverse_str_arr("hello") == ["o", "l", "l", "e", "h"])


def test_find_min_wrong_type():
    with pytest.raises(TypeError):
        find_min_index(":(")


def test_reverse_str_wrong_type():
    with pytest.raises(TypeError):
        reverse_str_arr(-2)

