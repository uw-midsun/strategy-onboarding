import pytest
from ..array import find_min_index, reverse_str_arr

# find_min_index tests:
def test_find_min_index():
    assert(find_min_index([7, -5, 6, -5, -4, 3]) == 1)
    assert(find_min_index([]) == -1)
    assert(find_min_index([1]) == 0)

def test_find_min_index_wrong_type():
    with pytest.raises(TypeError):
        find_min_index("13452")
    
def test_find_min_index_wrong_element_type():
    with pytest.raises(TypeError):
        find_min_index([7, 'a', 6, -5, -4, 3])

# revers_str_arr tests:
def test_reverse_str_arr():
    assert(reverse_str_arr("strategy") == ['y', 'g' ,'e' ,'t', 'a', 'r', 't', 's'])
    assert(reverse_str_arr("s") == ['s'])
    assert(reverse_str_arr("") == [])

def test_reverse_str_arr_wrong_type():
    with pytest.raises(TypeError):
        reverse_str_arr(54)
