from is_balanced import *
from tree import *

functions = [is_balanced, is_balanced_lame]

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_left(self, value):
        self.left = Node(value)

    def add_right(self, value):
        self.right = Node(value)

def test_empty():
    for f in functions:
        assert f(Node(0))

def test_single():
    root = Node(0)
    root.add_left(1)
    for f in functions:
        assert f(root)

def test_balanced():
    root = Node(0)
    root.add_left(1)
    root.add_right(2)
    root.left.add_left(3)
    for f in functions:
        assert f(root)

def test_balanced():
    root = Node(0)
    root.add_left(1)
    root.add_right(2)
    root.left.add_left(3)
    root.left.left.add_right(4)
    for f in functions:
        assert not f(root)
