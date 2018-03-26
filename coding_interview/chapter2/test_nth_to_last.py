from linked_list import *
from nth_to_last import *

def test_empty():
    head = None
    n = 5
    assert find_nth_to_last(head, n) is None

def test_single():
    head = Node(1)
    assert find_nth_to_last(head, 0) == 3

def test_single():
    l = list(range(10))
    head = list2linked(l)
    assert find_nth_to_last(head, 3) == 6

def test_single():
    l = list(range(10))
    head = list2linked(l)
    assert find_nth_to_last(head, 9) == 0
