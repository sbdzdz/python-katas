import pytest
from fill_zeros import *

functions = [fill_zeros, fill_zeros_pythonic]

def test_empty():
    for f in functions:
        assert f([[]]) == [[]]

def test_single_nonzero():
    for f in functions:
        assert f([[1]]) == [[1]]

def test_odd():
    for f in functions:
        arr = [[1, 2, 3],
               [4, 5, 6], 
               [7, 8, 0]]
        zer = [[1, 2, 0],
               [4, 5, 0],
               [0, 0, 0]]
        assert f(arr) == zer

def test_even():
    for f in functions:
        arr = [[1, 2, 0, 4],
               [5, 6, 7, 8], 
               [9, 0, 8, 7],
               [6, 5, 4, 3]]

        zer = [[0, 0, 0, 0],
               [5, 0, 0, 8], 
               [0, 0, 0, 0],
               [6, 0, 0, 3]]
        assert f(arr) == zer
