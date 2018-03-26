from linked_list import *
from detect_cycle import *

def test_simple():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = b
    assert detect_cycle(a) is b

def test_full_circle():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(4)
    f = Node(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = a
    assert detect_cycle(a) is a

def test_no_cycle():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    assert detect_cycle(a) is None

