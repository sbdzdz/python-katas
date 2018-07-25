from sort_stack import *
from random import shuffle

def test_empty():
    stack = Stack()
    assert sort_stack(stack).is_empty() 

def test_empty():
    to_sort = list(range(1000, 0, -1)) 
    shuffle(to_sort)

    stack = Stack()
    for element in to_sort:
        stack.push(element)
    ordered = sort_stack(stack)

    result = []
    while not ordered.is_empty():
        result.append(ordered.pop())
    assert result == list(range(1000, 0, -1))
