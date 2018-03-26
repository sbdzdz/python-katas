from anagrams import *

functions = [are_anagrams, are_anagrams_pythonic]

def test_empty():
    for f in functions:
        assert f('', '')

def test_one_empty():
    for f in functions:
        assert not f('', 'spam')

def test_different_length():
    for f in functions:
        assert not f('map', 'spam')

def test_non_anagrams():
    for f in functions:
        assert not f('spam', 'eggs')

def test_anagrams():
    for f in functions:
        assert f('maps', 'spam')

def test_extended_ascii():
    for f in functions:
        assert f('mäps', 'späm')
