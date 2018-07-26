from fibonacci import *

functions = [fibonacci_recursive, fibonacci_iterative]

def test_zeroth():
    for f in functions:
        assert f(0) == 1

def test_first():
    for f in functions:
        assert f(1) == 1

def test_first_ten():
    fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for n in range(10):
        for f in functions:
            assert f(n) == fibonacci[n]
