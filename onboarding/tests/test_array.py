import pytest
from ..array import find_min_index, reverse_str_arr


def test_min_index():
    assert(find_min_index([10,0,-1,-0,6]) == 2)
    assert(find_min_index([0,2,100,101,0]) == 0)
    assert(find_min_index([0,0,0,0,0]) == 0)


def test_min_index_empty():
    with pytest.raises(IndexError):
        find_min_index([])


def test_reverse_str_arr_standard():
    assert(reverse_str_arr("abc") == ['c','b','a'])
    assert(reverse_str_arr("!!-.2") == ['2', '.', '-', '!', '!'])
    assert(reverse_str_arr("abba") == ['a', 'b', 'b', 'a'])
    assert(reverse_str_arr("z") == ['z'])


def test_reverse_str_arr_empty():
    with pytest.raises(ValueError):
        reverse_str_arr("")

