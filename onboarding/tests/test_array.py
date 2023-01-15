# write some tests here!
import pytest
from ..array import find_min_index


def find_min_index():
    assert(find_min_index([1, 33, 1, -2, 0]) == 3)
    assert(find_min_index([0, 0, 0, 0, 0]) == 0)


def find_min_index_empty():
    with pytest.raises(TypeError):
        find_min_index([])


def reverse_str_arr():
    assert(reverse_str_arr("abc") == ['c', 'b', 'a'])
    assert(reverse_str_arr("abba") == ['a', 'b', 'b', 'a'])
    assert(reverse_str_arr("!!-.2") == ['2', '.', '-', '!', '!'])