import pytest
from ..array import find_min_index, reverse_str_arr

def test_find_min_index():
    assert(find_min_index([2,4,3,1,-4,3]) == 4)
    assert(find_min_index([4,-3,2,0,1]) == 1)


def test_find_min_index_length1():
    assert(find_min_index([1]) == 0)


def test_find_min_index_invalid():
    with pytest.raises(TypeError):
        find_min_index("abc")


def test_reverse_str_arr():
    assert(reverse_str_arr("abc") == ['c', 'b', 'a'])
    assert(reverse_str_arr("2!aks") == ['s', 'k', 'a', '!','2'])

def test_reverse_str_arr_invalid():
    with pytest.raises(TypeError):
        reverse_str_arr(2)
