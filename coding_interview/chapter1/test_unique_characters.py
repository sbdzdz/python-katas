from unique_characters import *

functions = [unique_characters, unique_characters_pythonic]


def test_empty():
    for f in functions:
        assert f("")


def test_unique():
    for f in functions:
        assert f("uniq")


def test_non_unique():
    for f in functions:
        assert not f("non_unique")
