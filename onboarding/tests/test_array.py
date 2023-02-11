# write some tests here!

import pytest
from ..array import find_min_index, reverse_str_arr

def test_find_min_index():
    assert(find_min_index([0,0,0,0,0]) == 0) # all zero
    assert(find_min_index([3,5,5,6,1,9]) == 4) # all positive
    assert(find_min_index([-5,-99,-1,-21,-14]) == 1) # all negative
    assert(find_min_index([12,-3,-7,0,23]) == 2) # mixed elements
    assert(find_min_index([4]) == 0) # single element

def test_reverse_string_arr():
    assert(reverse_str_arr("abc") == ['c', 'b', 'a'])
    assert(reverse_str_arr("abba") == ['a', 'b', 'b', 'a'])
    assert(reverse_str_arr("!!-.2") == ['2', '.', '-', '!', '!'])
    assert(reverse_str_arr("c") == ['c'])
    assert(reverse_str_arr("dddmd") == ['d', 'm', 'd', 'd', 'd'])