# write some tests here!
import pytest
from ..array import find_min_index, reverse_str_arr

int_arr = [7, 23, -4, 5, -4, -4, 7, 5, 23]
str = "bean"

def test_fibonacci_term():
    assert(find_min_index(int_arr) == 2)
    assert(reverse_str_arr(str) == ['n', 'a', 'e', 'b'])

def test_find_min_index_wrong_type():
    with pytest.raises(TypeError):
        find_min_index("13452")

def test_reverse_str_arr_wrong_type():
    with pytest.raises(TypeError):
        reverse_str_arr(42453)
