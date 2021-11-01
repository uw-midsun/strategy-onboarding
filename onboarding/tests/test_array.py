import pytest
from ..array import find_min_index, reverse_str_arr

'''
Testing find_min_index
'''

def test_min_index():
    assert(find_min_index([0, 5, 4, -1]) == 3)
    assert(find_min_index([-6, -4, -9, 11, 18]) == 2)
    assert(find_min_index([4]) == 0)
    assert(find_min_index([-1, -1, 4, -1]) == 0)


def test_min_index_empty():
    with pytest.raises(TypeError):
        find_min_index([])


def test_fibonacci_term_not_array():
    with pytest.raises(TypeError):
        find_min_index(":(")


def test_min_index_wrong_type_1():
    with pytest.raises(TypeError):
        find_min_index([":(", 0.0, "12"])

'''
Testing reverse_str_arr
'''

def test_reverse_str():
    assert(reverse_str_arr("") == [])
    assert(reverse_str_arr("string") == ['g', 'n', 'i', 'r', 't', 's'])
    assert(reverse_str_arr("word") == ['d', 'r', 'o', 'w'])


def test_reverse_str_wrong_type_1():
    with pytest.raises(TypeError):
        reverse_str_arr(0)

def test_reverse_str_wrong_type_2():
    with pytest.raises(TypeError):
        reverse_str_arr(["1", "2"])

