import pytest 
from ..array import find_min_index, reverse_str_arr

def test_find_min_index():
    assert(find_min_index([1, 33, 1, -2, 0]) == 3)
    assert(find_min_index([0, 0, 0, 0, 0]) == 0)

def test_find_min_index_empty():
    with pytest.raises(TypeError):
        find_min_index([])

def test_find_min_index_wrong_type():
    with pytest.raises(TypeError):
        find_min_index(":(")

def test_find_min_index_wrong_type2():
    with pytest.raises(TypeError):
        find_min_index(['1', '33', '1', '-2', '0'])

def test_reverse_string():
    assert(reverse_str_arr("abc") == ['c', 'b', 'a'] )
    assert(reverse_str_arr("abba") == ['a', 'b', 'b', 'a'] )
    assert(reverse_str_arr("!!-.2") == ['2', '.', '-', '!', '!'])

def test_reverse_string_wrong_type():
    with pytest.raises(TypeError):
        find_min_index(0)
