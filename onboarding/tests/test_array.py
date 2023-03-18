# write some tests here!
import pytest
from ..array import find_min_index

def test_find_min_index():
    assert(find_min_index([1,2,3,4,5,6,-1]) == 6)
    assert(find_min_index([-12312313,0,0,0,0]) == 0)
    assert(find_min_index([32, 23, 10, 1421341]) == 2)

def test_find_min_index_emptyArray():
    with pytest.raises(TypeError):
        find_min_index([])

def test_find_min_index_invalidType():
    with pytest.raises(TypeError):
        find_min_index("hello")

def test_find_min_index_invalidArray():
    with pytest.raises(TypeError):
        find_min_index([123, 12313, 9945, "hello", 12.1231])
    