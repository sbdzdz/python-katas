from list_to_bst import *

def test_empty():
    assert list_to_bst([]) is None

def test_single():
    result = list_to_bst([0])
    assert result.value == 0

def test_double():
    result = list_to_bst([0, 1])
    assert result.value == 1
    assert result.left.value == 0

def test_even():
    result = list_to_bst([0, 1, 2, 3, 4, 5])
    assert result.value == 3
    assert result.left.value == 1
    assert result.left.left.value == 0
    assert result.left.right.value == 2

    assert result.right.value == 5
    assert result.right.left.value == 4
