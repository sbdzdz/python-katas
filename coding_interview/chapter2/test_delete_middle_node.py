from linked_list import *
from delete_middle_node import *

def test_linked2list():
    l = [1, 2, 3, 4] 
    head = list2linked(l)
    node = head.next.next
    delete_middle_node(node)
    assert linked2list(head) == [1, 2, 4] 

def test_linked2list():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    head = list2linked(l)
    node = head.next.next.next
    delete_middle_node(node)
    assert linked2list(head) == [1, 2, 3, 5, 6, 7, 8, 9] 
