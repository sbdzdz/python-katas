from stack import *

classes = [Stack, NodeStack]

def test_is_empty():
    for Stack in classes:
        stack = Stack()
        assert stack.is_empty()

def test_push_pop():
    for Stack in classes:
        stack = Stack()
        stack.push(2)
        assert stack.pop() == 2
        assert stack.pop() == None 
        assert stack.is_empty()

def test_filo():
    for Stack in classes:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.pop() == None 
        assert stack.is_empty()
