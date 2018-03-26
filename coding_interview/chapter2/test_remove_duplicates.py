from linked_list import *
from remove_duplicates import *

def test_empty():
    head = list2linked([])
    head = remove_duplicates(head)
    assert head == None

def test_single():
    head = Node(1)
    head = remove_duplicates(head)
    assert head.value == 1
    assert head.next is None

def test_adjacent():
    l = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3]
    head = list2linked(l)
    head = remove_duplicates(head)
    assert linked2list(head) == [0, 1, 2, 3]

def test_non_adjacent():
    l = [1, 0, 0, 1, 0, 1, 1, 2, 2, 1, 3, 3, 2, 3]
    head = list2linked(l)
    head = remove_duplicates(head)
    assert linked2list(head) == [1, 0, 2, 3]

def test_no_duplicates():
    l = [2, 1, 4, 3, 7]
    head = list2linked(l)
    head = remove_duplicates(head)
    assert linked2list(head) == l 
