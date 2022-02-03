import pytest
from ..array import find_min_index, reverse_str_arr

# write some tests here!

# find_min_index
def test_find_min_index():
    assert(find_min_index([1, 33, 1, -2, 0]) == 3)
    assert(find_min_index([100, -1, -54, 30, 3000, -2000, 3]) == 5)
    assert(find_min_index([0, 0, 0, 0, 0]) == 0)
    assert(find_min_index([1]) == 0)

def test_find_min_index_empty_list():
    with pytest.raises(TypeError):
        test_find_min_index([])

def test_find_min_index_wrong_type():
    with pytest.raises(TypeError):
        test_find_min_index(123)


# reverse_str_arr
def test_reverse_str_arr():
    assert(reverse_str_arr('abc') == ['c', 'b', 'a'])
    assert(reverse_str_arr('!!-.2') == ['2', '.', '-', '!', '!'])
    assert(reverse_str_arr('abba') == ['a', 'b', 'b', 'a'])

def test_reverse_str_arr_empty_string():
    with pytest.raises(ValueError):
        reverse_str_arr('')

def test_reverse_str_arr_wrong_type():
    with pytest.raises(TypeError):
        reverse_str_arr(123)