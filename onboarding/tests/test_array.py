import pytest
from ..array import find_min_index, reverse_str_arr

def test_find_min_index():
    assert(find_min_index([1, 33, 1, -2, 0]) == 3)
    assert(find_min_index([0, 0, 0, 0, 0]) == 0)
    assert(find_min_index([1]) == 0)


def test_find_min_index_empty():
    assert(find_min_index([]) == -1)

def test_reverse_str_arr():
    assert(reverse_str_arr("a") == ['a'])
    assert(reverse_str_arr("abc") == ['c', 'b', 'a'])
    assert(reverse_str_arr("abba") == ['a', 'b', 'b', 'a'])
    assert(reverse_str_arr("!!-.2") == ['2', '.', '-', '!', '!'])

def test_reverse_str_arr_empty():
    assert(reverse_str_arr("") == [])



