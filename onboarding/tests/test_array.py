# write some tests here!
import pytest
from ..array import find_min_index, reverse_str_arr

def test_find_min_index():
    assert(find_min_index([1,2,3,4,5]) == 0)
    assert(find_min_index([0,0,0,0,0,0]) == 0)
    assert((find_min_index([543,234,23,54,23]) == 2))
    assert((find_min_index([-5, -4, -3, 0, 1]) == 0))
    assert((find_min_index([]) == None))

def test_reverse_str_arr():
    assert(reverse_str_arr('HELLO') == ['O', 'L', 'L', 'E', 'H'])
    assert(reverse_str_arr('AAAAAA') == ['A', 'A', 'A', 'A', 'A', 'A'])
