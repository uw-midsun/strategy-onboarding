# write some tests here!
import pytest
import sys
sys.path.append("..")
from ..array import find_min_index, reverse_str_arr


def test_find_min_index():
    assert(find_min_index([1, 33, 1, -2, 0]) == 3)
    assert(find_min_index([34, 33, 1, 2, 0]) == 4)


def test_reverse_str_arr():
    assert(reverse_str_arr("abc") == ['c', 'b', 'a'])
    assert(reverse_str_arr("!.$") == ['$', '.', '!'])

