# write some tests here!
import pytest
from ..array import find_min_index
from ..array import reverse_str_arr 


def test_find_min_index():
    assert(find_min_index([1, 2, 3, 3, 0]) == 4)
    assert(find_min_index([0]) == 0)
    assert(find_min_index([3, 9, 3, 3, 4, -3, 8, 4]) == 5)

def test_reverse_str_arr():
    assert(reverse_str_arr("strategy") == ['y', 'g', 'e', 't', 'a', 'r', 't', 's'])
    assert(reverse_str_arr('z') == ['z'])
    assert(reverse_str_arr("god") == ['d', 'o', 'g'])
    