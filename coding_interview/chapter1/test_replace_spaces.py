from replace_spaces import *

functions = [replace_spaces, replace_spaces_pythonic]


def test_empty():
    for f in functions:
        assert f("") == ""


def test_multiple_spaces():
    for f in functions:
        assert f("  ") == "%20%20"


def test_general_case():
    for f in functions:
        assert f("spam eggs bacon") == "spam%20eggs%20bacon"


def test_unicode():
    for f in functions:
        assert f("śpäm ęggś bącóń") == "śpäm%20ęggś%20bącóń"
