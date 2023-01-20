import pytest
from ..array_1 import find_min_index
from ..array_1 import reverse_str_arr

def test_find_min_index():
    assert(find_min_index([0, 1, 2, 3]) == 0)
    assert(find_min_index([1, 0, -1, 5, 2]) == 2)
def test_reverse_str_arr():
    assert(reverse_str_arr("hello") == ['o', 'l', 'l', 'e' , 'h'])
