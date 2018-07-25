from set_of_stacks import *

def test_is_empty():
    stack = SetOfStacks(1)
    stack = Stack()
    assert stack.is_empty()

def test_push_pop():
    stack = SetOfStacks(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == None 
    assert stack.is_empty()

def test_filo():
    stack = SetOfStacks(10)
    for element in range(1000):
        stack.push(element)
    for element in reversed(range(1000)):
        assert stack.pop() == element 
    assert stack.pop() == None 
    assert stack.is_empty()
