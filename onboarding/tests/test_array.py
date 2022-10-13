import pytest
from ..array import find_min_index

def test_find_min_index():
    assert(find_min_index([1, 33, 1, -2, 0]) == 3)
    assert(find_min_index([0, 0, 0, 0, 0]) == 0)

def test_find_min_index_no_array():
    with pytest.raises(TypeError):
        find_min_index([])