from linked_list import *

def test_node_empty():
    node = Node(0)
    assert node.value == 0
    assert node.next is None

def test_append():
    node = Node(0)
    node.append(1)
    assert node.value == 0
    assert node.next is not None
    assert node.next.value == 1
    assert node.next.next is None

def test_list2linked_empty():
    l = []
    head = list2linked(l)
    assert head is None

def test_list2linked():
    l = list(range(100)) 
    i = 0
    head = list2linked(l)
    while head.next is not None:
        assert head.value == l[i]
        head = head.next
        i += 1

def test_linked2list_empty():
    assert linked2list(None) == []

def test_linked2list():
    l = list(range(100))
    head = list2linked(l)
    assert linked2list(head) == l

def test_delete_node():
    l = [0, 1, 2, 3]
    head = list2linked(l)
    head = delete_node(head, 2)
    head = delete_node(head, 1)
    assert linked2list(head) == [0, 3] 
