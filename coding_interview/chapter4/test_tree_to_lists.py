from tree_to_lists import *
from tree import * 

functions = [tree_to_lists]

def test_empty():
    for f in functions:
        result = f(TreeNode(0))
        assert result[0].value == 0
        assert len(result) == 1

def test_single():
    root = TreeNode(0)
    root.add_left(1)
    for f in functions:
        result = f(root)
        assert result[0].value == 0
        assert result[1].value == 1

def test_balanced():
    root = TreeNode(0)
    root.add_left(1)
    root.add_right(2)
    root.left.add_left(3)
    root.left.left.add_right(4)
    for f in functions:
        result = f(root)
        assert result[0].value == 0
        assert result[1].value == 1
        assert result[1].next.value == 2
        assert result[2].value == 3
        assert result[3].value == 4
