from minstack import *

def test_is_empty():
    stack = MinStack()
    assert stack.is_empty()

def test_push_pop():
    stack = MinStack()
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == None 
    assert stack.is_empty()

def test_filo():
    stack = MinStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == None 
    assert stack.is_empty()

def test_min():
    stack = MinStack()
    stack.push(4)
    assert stack.get_min() == 4
    stack.push(3)
    assert stack.get_min() == 3
    stack.push(3)
    assert stack.get_min() == 3
    stack.push(2)
    assert stack.get_min() == 2
    stack.pop()
    assert stack.get_min() == 3
    stack.pop()
    assert stack.get_min() == 3
    stack.pop()
    assert stack.get_min() == 4
    stack.pop()
    assert stack.get_min() is None 
