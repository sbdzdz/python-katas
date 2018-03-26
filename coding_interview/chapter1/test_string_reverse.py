import pytest
from string_reverse import *

functions = [reverse_cstyle, reverse_cstyle_pythonic, reverse_cstyle_while]

def test_empty():
    for f in functions:
        assert f('') == ''

def test_single_character():
    for f in functions:
        assert f('0') == '0'

def test_non_empty():
    for f in functions:
        assert f('test0') == 'tset0'
