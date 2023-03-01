import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import pytest

from fibonacci import fibonacci_term


def test_fibonacci_term():
    assert(fibonacci_term(3) == 2)
    assert(fibonacci_term(5) == 5)
    assert(fibonacci_term(22) == 17711)


def test_fibonacci_term_zero():
    with pytest.raises(TypeError):
        fibonacci_term(0)


def test_fibonacci_term_negative():
    with pytest.raises(TypeError):
        fibonacci_term(-2)


def test_fibonacci_term_wrong_type():
    with pytest.raises(TypeError):
        fibonacci_term(":(")
