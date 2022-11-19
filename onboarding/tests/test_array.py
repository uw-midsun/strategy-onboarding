# write some tests here!
import pytest
from ..array import find_min_index, reverse_str_arr


def test_find_min_index():
    assert(find_min_index([-2, 0, 2]) == 0)
    assert(find_min_index([9, 8, 7]) == 2)
    assert(find_min_index([-2, 7, 3, 8, -12, 0]) == 4)


def test_find_min_index_str():
    with pytest.raises(TypeError):
        find_min_index([1, 2, "3"])



def test_reverse_str_arr():
    assert(reverse_str_arr("hello") == ["o","l","l","e","h"])
    assert(reverse_str_arr("54321") == ["1","2","3","4","5"])
    assert(reverse_str_arr("why?!") == ["!","?","y","h","w"])



def test_reverse_str_arr_int():
    with pytest.raises(TypeError):
        reverse_str_arr(123)



