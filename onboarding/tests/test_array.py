# write some tests here!
import pytest
from ..array import reverse_str_arr  
from ..array import find_min_index

def test_find_main_index():
    assert(find_min_index([0, 0, 0, 0, 0]) == 0)
    assert(find_min_index([1, 33, 1, -2, 0]) == 3)

def test_reverse_str_arr():
    assert(reverse_str_arr("abc") == ['c', 'b', 'a'])
    assert(reverse_str_arr("abba") == ['a', 'b', 'b', 'a'])
    assert(reverse_str_arr("!!-.2") == ['2', '.', '-', '!', '!'])

    
