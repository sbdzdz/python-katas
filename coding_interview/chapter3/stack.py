class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not self.stack

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class NodeStack(object):
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is not None:
            value = self.top.value
            self.top = self.top.next
            return value
        return None

    def is_empty(self):
        return self.top is None
